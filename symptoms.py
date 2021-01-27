from typing import List, Any, Union

import numpy as np

symptoms = [
    "wheezing",
    "cough",
    "chest discomfort",
    "Extremities",
    "leg pain",
    "chronic pain",
    "loss of smell",
    "chills",
    "Fever",
    "fever",
    "Paresthesia",
    "numbness",
    "tingling",
    "electric tweaks",
    "Light-headed",
    "Dizzy",
    "dry mouth",
    "Nauseated",
    "nausea",
    "Sick",
    "like I have the flu",
    "vomit",
    "Short of breath",
    "Sleepy",
    "Sweaty",
    "Thirsty",
    "Tired",
    "Weak",
    "Breathe normally",
    "Hear normally",
    "losing hearing",
    "sounds are too loud",
    "ringing or hissing in my ears",
    "Move one side – arm and/or leg",
    "Pass a bowel action normally",
    "Pass urine normally",
    "Remember normally",
    "See properly",
    "Blindness",
    "blurred vision",
    "double vision",
    "Sleep normally",
    "Smell things normally",
    "Speak normally",
    "Stop passing watery bowel actions",
    "Stop scratching",
    "Stop sweating",
    "Swallow normally",
    "Taste properly",
    "Walk normally",
    "Write normally",
    "Medical symptoms",
    "anorexia",
    "weight loss",
    "cachexia",
    "chills and shivering",
    "convulsions",
    "deformity",
    "discharge",
    "dizziness",
    "Vertigo",
    "fatigue",
    "malaise",
    "asthenia",
    "hypothermia",
    "muscle weakness",
    "pyrexia",
    "hematuria",
    "impotence",
    "polyuria",
    "retrograde ejaculation",
    "strangury",
    "urethral discharge",
    "urinary frequency"
    "urinary incontinence",
    "urinary retention",
    "sweats",
    "swelling",
    "lymph node",
    "weight gain",
    "Cardiovascular",
    "chest pain",
    "palpitations"
    "Nose",
    "throat",
    "dry mouth",
    "hearing loss",
    "nasal discharge",
    "sore throat",
    "toothache",
    "tinnitus",
    "Gastrointestinal",
    "abdominal pain",
    "bloating",
    "belching",
    "bleeding",
    "Hematemesis",
    "blood in stool",
    "hematochezia",
    "constipation",
    "diarrhea",
    "fecal incontinence",
    "flatulence",
    "heartburn",
    "nausea",
    "vomiting",
    "Hair",
    "nail",
    "abrasion",
    "anasarca"
    "bleeding into the skin",
    "blister"
    "edema",
    "itching",
    "laceration",
    "rash",
    "urticaria",
    "Neurological",
    "abnormal posturing",
    "amnesia",
    "anomia",
    "confusion",
    "hallucination",
    "muscle cramps",
    "tremor",
    "flapping tremor",
    "insomnia",
    "loss of consciousness",
    "neck stiffness",
    "abnormal vaginal bleeding",
    "pregnancy",
    "painful intercourse",
    "pelvic pain",
    "vaginal discharge",
    "vision",
    "wheezing",
    "anxiety",
    "depression",
    "delusion",
    "euphoria",
    "irritability",
    "mania",
    "paranoid ideation",
    "phobia",
    "suicidal",
    "Pulmonary",
    "sputum production",
    "back pain",
    "back ache"
];

