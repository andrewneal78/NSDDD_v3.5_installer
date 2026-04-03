"""
Configuration for NSDDD v3.5 Installation

This module contains all configuration settings for downloading and installing
the National Security Documents Dataset (NSDDD) version 3.5 from Edinburgh DataShare.
"""

# DataShare API endpoints
DATASHARE_API_BASE = 'https://datashare.ed.ac.uk/rest'

# DataShare handle for NSDDD v3.5
# https://datashare.ed.ac.uk/handle/10283/9182
DATASHARE_HANDLE = '10283/9182'

# Construct base URL for files
DATASHARE_ITEM_URL = f'{DATASHARE_API_BASE}/handle/{DATASHARE_HANDLE}'

# Download specifications
DOWNLOADS = {
    # REQUIRED downloads (essential for semantic search)
    'model_files': {
        'filename': 'model_files.zip',
        'size_mb': 4116.314,
        'size_gb': 4.019838,
        'extract_to': 'model/',
        'required': True,
        'description': 'Model files: MPNet embeddings and segment data (~4.6GB uncompressed)'
    },
    'metadata': {
        'filename': 'metadata.zip',
        'size_mb': 0.073,
        'size_gb': 0.000071,
        'extract_to': 'metadata/',
        'required': True,
        'description': 'Metadata: document and country information'
    },
    'whats_new': {
        'filename': 'WHATS_NEW_IN_NSDDD_V3.5.md',
        'size_mb': 0.016,
        'size_gb': 0.000016,
        'extract_to': 'documentation/',
        'required': True,
        'description': 'Complete overview of v3.5 improvements and features'
    },
    'inclusion_criteria': {
        'filename': 'dataset_inclusion_criteria.md',
        'size_mb': 0.024,
        'size_gb': 0.000024,
        'extract_to': 'documentation/',
        'required': True,
        'description': 'Document selection criteria and methodology'
    },
    'readme': {
        'filename': 'README.txt',
        'size_mb': 0.010,
        'size_gb': 0.000010,
        'extract_to': 'documentation/',
        'required': True,
        'description': 'Quick start guide'
    },
    'citation': {
        'filename': 'CITATION.txt',
        'size_mb': 0.004,
        'size_gb': 0.000004,
        'extract_to': 'documentation/',
        'required': True,
        'description': 'Citation formats for research use'
    },
    'license': {
        'filename': 'LICENSE.txt',
        'size_mb': 0.006,
        'size_gb': 0.000006,
        'extract_to': 'documentation/',
        'required': True,
        'description': 'CC BY 4.0 license terms'
    },

    # OPTIONAL downloads (user chooses which to download)
    'clean_text': {
        'filename': 'clean_text_documents_English_and_translated.zip',
        'size_mb': 43.646,
        'size_gb': 0.042623,
        'extract_to': 'documents/',
        'optional': True,
        'description': '671 plain text documents (English + translated)'
    },
    'spacy': {
        'filename': 'spacy_documents.zip',
        'size_mb': 46.064,
        'size_gb': 0.044984,
        'extract_to': 'documents/',
        'optional': True,
        'description': '671 sentence-segmented documents'
    },
    'pdf_originals': {
        'filename': 'pdf_originals.zip',
        'size_mb': 7101.902,
        'size_gb': 6.935451,
        'extract_to': 'documents/',
        'optional': True,
        'description': '671 original PDFs organized by country'
    },
    'original_language': {
        'filename': 'original_language_documents.zip',
        'size_mb': 10.001,
        'size_gb': 0.009766,

        'extract_to': 'documents/',
        'optional': True,
        'description': 'Original language plain text files'
    },
    'original_language_spacy': {
        'filename': 'original_language_spacy.zip',
        'size_mb': 10.476,
        'size_gb': 0.010231,
        'extract_to': 'documents/',
        'optional': True,
        'description': 'Original language sentence-segmented files'
    }
}

# System requirements
PYTHON_VERSION_MIN = (3, 9)
DISK_SPACE_REQUIRED_MIN_GB = 15  # Minimum for model files only
RAM_REQUIRED_GB = 16  # Recommended for loading 12GB embedding file

# Installation directory naming
DEFAULT_INSTALL_DIR = 'NSDDD_v3.5_workspace'

# Dependencies (from requirements.txt)
CORE_DEPENDENCIES = [
    'sentence-transformers>=2.2.0',
    'numpy>=1.24.0',
    'scipy>=1.10.0',
    'networkx>=3.0',
    'ipywidgets>=8.0.0',
    'tqdm>=4.65.0',
    'requests>=2.31.0',
    'psutil>=5.9.0',
    'pandas>=1.5.0',
    'matplotlib>=3.7.0',
    'seaborn>=0.12.0',
]

# Optional dependencies for future extensions
OPTIONAL_DEPENDENCIES = [
]

# Download and verification settings
CHUNK_SIZE = 8192  # Bytes per chunk for downloads
RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 30

# Dataset information
DATASET_NAME = 'National Security and Defence Documents Dataset (1987-2025) v3.5'
DATASET_DOCUMENTS = 671
DATASET_COUNTRIES = 118
DATASET_YEARS = '1987–2025'
DATASET_SEGMENTS = 787844
DATASET_ENCODING_DIM = 768
