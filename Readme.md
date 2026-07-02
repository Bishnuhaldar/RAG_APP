my-rag-app/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI entry point
│   ├── config.py                  # Settings with pydantic-settings
│   │
│   ├── core/                      # Core RAG logic
│   │   ├── ingestion.py           # Load & chunk documents
│   │   ├── embeddings.py          # Generate embeddings
│   │   ├── retriever.py           # Search vector DB
│   │   ├── generator.py           # LLM response generation
│   │   └── rag_pipeline.py        # End-to-end RAG flow
│   │
│   ├── api/
│   │   ├── routes/
│   │   │   ├── ingest.py          # POST /ingest
│   │   │   ├── query.py           # POST /query
│   │   │   └── health.py          # GET /health
│   │   └── schemas.py             # Request/response models
│   │
│   ├── db/
│   │   ├── vector_store.py        # Vector DB client (Chroma/Qdrant)
│   │   └── models.py              # Database models (if using SQL)
│   │
│   └── utils/
│       ├── logger.py              # Logging setup
│       └── helpers.py             # Common utilities
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_api.py
│
├── data/                          # Local data (gitignored)
│   └── documents/
│
├── deployments/                   # Deployment configs
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .env                           # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
