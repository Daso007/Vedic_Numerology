# AI-Powered Vedic & Chinese Numerology Platform

##url https://vedicnumerology.streamlit.app/
## Project Overview 
This project is an interactive web application that provides personalized numerology and career guidance. It synthesizes principles from both Vedic (Indian) and Western Chinese numerology systems, offering a unique and comprehensive perspective on an individual's life path, innate talents, potential challenges, and environmental alignments.

The application leverages a large language model (LLM) powered by Google's Gemini AI, utilizing a custom-curated knowledge base derived from authoritative numerology texts.

## Features
- **Personalized Numerology Analysis:** Generate detailed reports based on a user's date of birth and gender.
- **Multi-System Integration:** Combines calculations and interpretations from:
    -   **Moolank (Psychic Number):** Your innate personality and talents.
    -   **Bhagyank (Destiny/Life Path Number):** Your life's purpose and destined path.
    -   **Kua Number (Feng Shui/Luck Number):** Your auspicious directions for various life aspects.
    -   **Lo Shu Grid Analysis:** A visual representation of your core numbers, revealing strengths, weaknesses, and life lessons.
-   **Dynamic Career Guidance:** Tailored advice for professionals (seeking alignment with current career) or students (exploring future options), based on their unique numerological profile.
-   **Interactive Web Interface:** User-friendly experience built with Streamlit.

## How It Works
1.  **Input Collection:** Users provide their Date of Birth, Gender, and a brief description of their career history or study interests.
2.  **Numerological Calculation:** A Python backend calculates core numbers:
    -   Moolank (Psychic Number) from the day of birth.
    -   Bhagyank (Destiny Number) from the full date of birth.
    -   Kua Number from the birth year and gender, following specific Vedic/Chinese rules.
    -   A comprehensive Lo Shu Grid is generated, populated with digits from the date of birth, Moolank, Bhagyank, and Kua Number.
3.  **Knowledge Retrieval:** The application accesses a pre-processed and structured knowledge base containing detailed interpretations of numbers, grids, and arrows from selected numerology texts.
4.  **AI-Powered Analysis:** A sophisticated prompt is crafted, combining the user's calculated numerological data with the relevant knowledge from the database. This prompt is sent to Google's Gemini AI model.
5.  **Report Generation:** The AI processes the prompt and generates a multi-section, personalized numerology report, formatted for easy understanding.

## Live Application
Experience the app live here: **[Your Streamlit App URL Here]**
*(Remember to replace `[Your Streamlit App URL Here]` with the actual URL you got from Streamlit Cloud, e.g., `https://dasoai-numerolog.streamlit.app/`)*

## Getting Started (Local Development)

To run this project locally on your machine, follow these steps:

### Prerequisites
- Python 3.8+ installed
- Git installed (optional, for cloning)

### Setup
1.  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/YourGitHubUsername/Numerology_Platform_V2.git
    cd Numerology_Platform_V2
    ```
    *(Replace `YourGitHubUsername` with your actual GitHub username)*

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   On Windows: `.\venv\Scripts\activate`
    -   On macOS/Linux: `source venv/bin/activate`

4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure you run `pip freeze > requirements.txt` first if you made local changes after deployment)

5.  **Get your Google AI API Key:**
    -   Go to [https://makersuite.google.com/](https://makersuite.google.com/)
    -   Create a free account and generate an API key.

6.  **Configure your API Key:**
    -   Open `app_v2.py`.
    -   Find the line `GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY_GOES_HERE"`
    -   Replace `YOUR_GOOGLE_API_KEY_GOES_HERE` with your actual API key. **Keep this key confidential.**

### Running the Application
To launch the web application:
```bash

streamlit run app_v2.py
