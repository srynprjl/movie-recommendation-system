# Movie Recommendation System

A content-based movie recommendation system that suggests movies similar to a user's selection. The system uses natural language processing and cosine similarity to find relationships between movies based on their genres, keywords, cast, and crew.

## Features

- **Interactive UI**: Built with Streamlit for a smooth and responsive user experience.
- **Content-Based Filtering**: Recommends movies based on metadata similarity.
- **Movie Posters**: Fetches and displays movie posters using The Movie Database (TMDB) API.
- **Detailed Information**: Provides recommendations with titles and visual previews.

## Architecture

1.  **Data Preprocessing**: The system processes the TMDB 5000 Movie Dataset, cleaning metadata like genres, keywords, cast, and crew.
2.  **Vectorization**: It uses `CountVectorizer` from `scikit-learn` to convert textual metadata into vectors.
3.  **Similarity Calculation**: Cosine similarity is used to calculate the distance between movie vectors.
4.  **Backend**: A Python script (`main.py`) handles the recommendation logic and TMDB API calls.
5.  **Frontend**: Streamlit provides the web interface.

## Installation

### Prerequisites

- Python 3.13 or higher
- A TMDB API Key (Get it from [themoviedb.org](https://www.themoviedb.org/documentation/api))

### Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/srynprjl/movie-recommendation-system
    cd movie-recommendation-system
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**:
    Create a `.env` file in the root directory and add your TMDB API Key:
    ```env
    API_KEY=your_tmdb_api_key_here
    ```

## Usage

### 1. Generate the Model (Optional)

If the `.pkl` files are not present, you can generate them by running the notebook:
`notebook/reccomendation_system.ipynb`

This will create `movies.pkl` and `similarity.pkl`.

### 2. Run the Application

Start the Streamlit app:
```bash
streamlit run main.py
```

Open your browser and navigate to `http://localhost:8501`.

## Dataset

The project uses the **TMDB 5000 Movie Dataset**, which includes information on 5000 movies, such as budget, genres, popularity, release date, and more.

## Technologies Used

- **Python**: Core programming language.
- **Pandas & NumPy**: Data manipulation and numerical computations.
- **Scikit-Learn**: Vectorization and similarity metrics.
- **NLTK**: Natural Language Toolkit for text processing.
- **Streamlit**: Web application framework.
- **TMDB API**: For fetching movie posters and metadata.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
