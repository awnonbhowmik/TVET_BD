"""
Data loading and preprocessing utilities for the TVET Bangladesh analysis.
"""

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data" / "TVET_Teachers.xlsx"
FULL_SURVEY_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "State of Technical and Vocational Education and Training (TVET) in Bangladesh (Responses).xlsx"
)
STUDENT_SURVEY_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "Challenges Faced by Students in Polytechnic Institutes of Bangladesh (Responses).xlsx"
)

COLUMN_MAP = {
    "Select your Educational Qualification.": "Education",
    "Have you completed any training, certifications and/or workshops?": "TrainingCompleted",
    "Select the training/certifications/workshops completed:": "TrainingDetails",
    "Please select your Institution": "Institution",
    "Do you apply Bloom's Taxonomy in your classroom?": "BloomsTaxonomy",
    "Do you use Blended Learning?": "BlendedLearning",
    "Select Department:": "Department",
}

TRAININGS = [
    "Advanced pedagogy in TVET",
    "Basic procurement training",
    "Basic training course",
    "Foundation training",
    "International training",
    "NTVQF Level 1",
    "NTVQF Level 2",
    "NTVQF Level 3",
    "Procuring Entity",
    "Other Training",
]


def load_data(path=None):
    """Load the TVET teacher dataset and rename columns.

    Parameters
    ----------
    path : str or Path, optional
        Path to the Excel file. Defaults to data/TVET_Teachers.xlsx.

    Returns
    -------
    pd.DataFrame
    """
    path = Path(path) if path else DATA_PATH
    df = pd.read_excel(path)
    return df.rename(columns=COLUMN_MAP)


def get_training_counts(df):
    """Count how many respondents completed each training type.

    Matching is case-insensitive substring search. A single teacher
    can appear in multiple training categories.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataset as returned by load_data().

    Returns
    -------
    pd.DataFrame
        Columns ['Training', 'Count'], sorted by Count descending.
    """
    trainings_lower = [t.lower() for t in TRAININGS]
    counts = {t: 0 for t in TRAININGS}
    for entry in df["TrainingDetails"].fillna(""):
        entry_lower = entry.lower()
        for i, t_lower in enumerate(trainings_lower):
            if t_lower in entry_lower:
                counts[TRAININGS[i]] += 1
    return (
        pd.DataFrame(list(counts.items()), columns=["Training", "Count"])
        .sort_values("Count", ascending=False)
        .reset_index(drop=True)
    )


def load_data_with_timestamp(path=None, full_survey_path=None):
    """Load the cleaned TVET teacher dataset with survey Timestamp added.

    The Timestamp comes from the original full survey file
    (State of TVET in Bangladesh Responses.xlsx), whose rows are confirmed to
    be in the same order as TVET_Teachers.xlsx.

    Parameters
    ----------
    path : str or Path, optional
        Path to TVET_Teachers.xlsx. Defaults to DATA_PATH.
    full_survey_path : str or Path, optional
        Path to the full survey file. Defaults to FULL_SURVEY_PATH.

    Returns
    -------
    pd.DataFrame  — same as load_data() but with a 'Timestamp' column prepended.
    """
    df = load_data(path)
    full = pd.read_excel(full_survey_path or FULL_SURVEY_PATH, usecols=["Timestamp"])
    df.insert(0, "Timestamp", pd.to_datetime(full["Timestamp"]))
    return df


STUDENT_COLUMN_MAP = {
    "1. What is your Gender?": "Gender",
    "2. What is your family\u2019s approximate monthly income?": "FamilyIncome",
    "3. What is your family\u2019s primary source of income?": "IncomeSource",
    "4. Do you work?": "WorksWhileStudying",
    "5. If you\u2019ve ever faced financial difficulties, how have they impacted your ability?":
        "FinancialImpact",
    "6. Are you aware of any scholarships or financial aid provided for polytechnic students?":
        "ScholarshipAwareness",
    "6. How would you rate the availability of resources (e.g., lab equipment, computers, internet) needed for your studies?":
        "ResourceAvailability",
    "8. Do you have access to the necessary study materials and resources outside of class?":
        "ExternalResourceAccess",
    "8. Are you confident that this education will help you secure a job after graduation? (1-10 scale, from Not at all confident to Very confident)":
        "JobConfidence",
    "7. Do you feel society looks down on polytechnic education or considers it inferior to other forms of higher education?":
        "SocialStigma",
    "8. Have you ever faced negative comments or attitudes from friends, family, or community members because you attend a polytechnic?":
        "NegativeComments",
    "9. Does this social perception affect your motivation to continue your studies?":
        "MotivationAffected",
    "13. Do you feel supported by your family in your choice to study at a polytechnic institute?":
        "FamilySupport",
    "14. Would financial or moral support from your family make a difference in your studies?":
        "FamilySupportImpact",
    "10. How often do you feel stressed about your studies and future career prospects?":
        "StressFrequency",
    "11. What is the biggest challenge you face in your polytechnic education?":
        "BiggestChallenge",
    "Please select your department.": "Department",
    "Please select your Institution": "Institution",
}


def load_student_data(path=None):
    """Load and clean the student challenges survey dataset.

    Drops the consent text column (column index 1) and the empty
    last column (Column 19). Renames all question columns to short names.

    Parameters
    ----------
    path : str or Path, optional
        Defaults to STUDENT_SURVEY_PATH.

    Returns
    -------
    pd.DataFrame  — 1,212 rows, 19 columns (Timestamp + 17 question fields + Institution)
    """
    path = Path(path) if path else STUDENT_SURVEY_PATH
    df = pd.read_excel(path)
    # Drop the consent text column and the empty trailing column
    drop_cols = [df.columns[1], df.columns[20]]
    df = df.drop(columns=drop_cols)
    df = df.rename(columns=STUDENT_COLUMN_MAP)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    return df


def get_crosstab_pct(df, row_col, col_col, normalize="index"):
    """Return a row-normalised cross-tabulation as percentages.

    Parameters
    ----------
    df : pd.DataFrame
    row_col : str
        Column name for rows.
    col_col : str
        Column name for columns.
    normalize : str
        Passed to pd.crosstab (default 'index' = row percentages).

    Returns
    -------
    pd.DataFrame  (values are percentages 0–100)
    """
    ct = pd.crosstab(df[row_col], df[col_col], normalize=normalize)
    return (ct * 100).round(1)
