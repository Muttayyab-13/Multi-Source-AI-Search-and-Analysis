from openai import OpenAI
from typing import List, Dict
from models.data_models import SearchResult, SearchAnalysis, SourceAnalysis
from config.settings import Config

class AIAnalyzer:
    def __init__(self):
        self.config = Config()
        self.client = OpenAI(api_key=self.config.OPENAI_API_KEY)

    def generate_analysis(self, query: str,
                          documents: List[SearchResult],
                          source_analyses: Dict[str, SourceAnalysis]) -> SearchAnalysis:
        context = self._prepare_context(query, documents, source_analyses)
        summary = self._generate_summary(query, context)
        insights = self._generate_insights(query, context)
        return SearchAnalysis(
            query=query,
            overall_summary=summary,
            key_insights=insights,
            source_analyses=list(source_analyses.values())
        )

    def _prepare_context(self, query, documents, source_analyses) -> str:
        parts = [f"Search Query: {query}", f"Total Documents Analyzed: {len(documents)}", ""]
        for stype, analysis in source_analyses.items():
            parts.extend([
                f"{stype.upper()} Analysis:",
                f"- Total results: {analysis.total_results}",
                f"- Sentiment: Positive: {analysis.sentiment.positive:.2f}, "
                f"Negative: {analysis.sentiment.negative:.2f}, "
                f"Neutral: {analysis.sentiment.neutral:.2f}",
                f"- Key themes: {', '.join(analysis.key_themes)}",
                f"- Sample content: {analysis.sample_content[0] if analysis.sample_content else 'N/A'}",
                ""
            ])
        return "\n".join(parts)

    def _generate_summary(self, query: str, context: str) -> str:
        prompt = f"""
        Based on the following search results for "{query}", provide a comprehensive summary:

        {context}

        Include main topics, sentiment, differences between sources,
        and notable trends. (2–3 paragraphs)
        """
        try:
            resp = self.client.chat.completions.create(
                model=self.config.LLM_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.config.MAX_TOKENS // 2,
                temperature=self.config.TEMPERATURE
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating summary: {e}")
            return self._generate_fallback_summary(query, context)

    def _generate_insights(self, query: str, context: str) -> List[str]:
        prompt = f"""
        Based on the search results for "{query}", identify 3–5 key insights:

        {context}

        Format as a numbered list.
        """
        try:
            resp = self.client.chat.completions.create(
                model=self.config.LLM_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.config.MAX_TOKENS // 2,
                temperature=self.config.TEMPERATURE
            )
            insights_text = resp.choices[0].message.content.strip()
            insights = []
            for line in insights_text.splitlines():
                line = line.strip()
                if line and (line[0].isdigit() or line.startswith(("-", "•"))):
                    insight = line.lstrip("0123456789.-• ").strip()
                    if insight:
                        insights.append(insight)
            return insights[:5]
        except Exception as e:
            print(f"Error generating insights: {e}")
            return self._generate_fallback_insights(query)

    def answer_followup_question(self, question: str,
                                 relevant_docs: List[SearchResult]) -> str:
        context_docs = [
            f"Source: {doc.source_type} - {doc.title}\nContent: {doc.content[:300]}..."
            for doc in relevant_docs[:5]
        ]
        context = "\n\n".join(context_docs)
        prompt = f"""
        Based on the following search results, answer this question: {question}

        Context:
        {context}

        Provide a comprehensive answer and cite sources (youtube, news, twitter).
        """
        try:
            resp = self.client.chat.completions.create(
                model=self.config.LLM_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.config.MAX_TOKENS // 3,
                temperature=self.config.TEMPERATURE
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error answering question: {e}")
            return f"Unable to process the question '{question}' at the moment."
