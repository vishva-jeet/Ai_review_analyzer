# Ai_review_analyzer
An AI-powered product review analyzer that processes Amazon product reviews and uses Groq's LLaMA model to generate concise one-line summaries, exporting the results to a structured CSV file.

## Project Structure
ai-review-analyzer/
│
├── main.py          # Entry point, orchestrates the pipeline
├── scraper.py       # Selenium-based Amazon review scraper
├── model_llm.py     # Groq LLM summarization logic
├── utils.py         # Text cleaning utilities
├── requirements.txt # Project dependencies
├── .env             # API keys (not committed to git)
└── output.csv       # Generated results





## Tech Stack
- **Groq API** (LLaMA 3.1) — AI summarization
- **Selenium** — Dynamic page scraping
- **BeautifulSoup** — HTML parsing
- **Pandas** — Data handling & CSV export
- **Python Dotenv** — Secure API key management


## Project Structure
ai-review-analyzer/
│
├── main.py          # Entry point, orchestrates the pipeline
├── scraper.py       # Selenium-based Amazon review scraper
├── model_llm.py     # Groq LLM summarization logic
├── utils.py         # Text cleaning utilities
├── requirements.txt # Project dependencies
├── .env             # API keys (not committed to git)
└── output.csv       # Generated results









## How to Run


1. **Clone the repo and install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Add your Groq API key in `.env`:**
```env
GROQ_API_KEY=your_groq_api_key
```

3. **Run the project:**
```bash
python main.py
```

4. **Check results in `output.csv`**

## Output Format
| review | rating | summary |
|--------|--------|---------|
| Full review text... | 5.0 out of 5 stars | One line AI summary |

## Get Groq API Key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up and create an API key
3. Paste it in your `.env` file

## Note
Amazon actively blocks automated scraping. For demo purposes,
the pipeline runs on a sample dataset showcasing the full AI summarization pipeline. 
The scraper module is production-ready and can be adapted for platforms that permit scraping or via Amazon's official Product Advertising API.

## Author
Vishvajeet
