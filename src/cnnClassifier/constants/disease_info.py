"""
This module contains comprehensive information about chicken diseases
that can be detected by the model.
"""

DISEASE_INFO = {
    "Coccidiosis": {
        "description": "Coccidiosis is a parasitic disease that affects the intestinal tract of chickens. It is caused by protozoa of the genus Eimeria. The disease can cause significant economic losses in poultry production due to reduced growth rates, increased mortality, and treatment costs.",
        "severity": "high",
        "symptoms": [
            "Diarrhea (often bloody)",
            "Weight loss",
            "Decreased feed intake",
            "Dehydration",
            "Ruffled feathers",
            "Depression",
            "Huddling behavior",
            "Reduced growth rate",
            "Increased mortality in severe cases"
        ],
        "transmission": [
            "Direct contact with infected birds",
            "Contaminated feed and water",
            "Contaminated equipment and bedding",
            "Wild birds and rodents",
            "Insects and other vectors"
        ],
        "incubation": "4-7 days",
        "prevention": [
            "Maintain strict biosecurity measures",
            "Regular cleaning and disinfection of facilities",
            "Proper waste management",
            "Control of wild birds and rodents",
            "Vaccination programs",
            "Regular health monitoring",
            "Quarantine new birds"
        ],
        "treatment": [
            "Administer anticoccidial medications as prescribed",
            "Provide supportive care and hydration",
            "Isolate affected birds",
            "Clean and disinfect the environment",
            "Monitor response to treatment",
            "Adjust feed and water management",
            "Implement preventive measures"
        ],
        "risk_factors": [
            "High stocking density",
            "Poor ventilation",
            "Wet litter conditions",
            "Stress from environmental changes",
            "Poor nutrition",
            "Immune system suppression"
        ],
        "economic_impact": [
            "Reduced growth rates",
            "Increased mortality",
            "Higher treatment costs",
            "Reduced egg production",
            "Poor feed conversion",
            "Increased medication costs"
        ],
        "diagnostic_methods": [
            "Clinical signs observation",
            "Fecal examination",
            "Post-mortem examination",
            "Histopathology",
            "PCR testing",
            "Serological tests"
        ]
    },
    "Normal": {
        "description": "No signs of disease detected. The chicken appears to be healthy.",
        "severity": "none",
        "symptoms": [],
        "transmission": [],
        "incubation": "N/A",
        "prevention": [
            "Maintain regular health checks",
            "Follow vaccination schedule",
            "Provide balanced nutrition",
            "Ensure clean water supply",
            "Maintain proper housing conditions",
            "Practice good biosecurity"
        ],
        "treatment": [],
        "risk_factors": [],
        "economic_impact": [],
        "diagnostic_methods": []
    }
}

# Add Healthy as an alias for Normal
DISEASE_INFO["Healthy"] = DISEASE_INFO["Normal"] 