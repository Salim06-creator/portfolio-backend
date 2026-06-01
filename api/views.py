from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def profile(request):
    data = {
        "name": "Salim Khamis Salim",
        "course": "Data Science",

        "bio": "Passionate about AI, web development, and cloud computing.",

        "skills": [
            "Python",
            "Django",
            "React",
            "Machine Learning",
             "Power BI",
             "SQL",
             "Excell",
             "Streamlit"
        ],

        "contact": {
            "email": "salim@gmail.com",
            "phone": "+255 777 089 837",
            "location": "Zanzibar, Tanzania"
        },

        "socials": {
            "github": "https://github.com/yourusername",
            "linkedin": "https://linkedin.com/in/yourusername"
        }
    }

    return Response(data)


@api_view(['GET'])
def projects(request):
    data = [
        {
            "title": "EMIS System",
            "description": "Education management system"
        },

        {
            "title": "Car Booking System",
            "description": "Online vehicle reservation platform"
        },

        {
            "title": "Anomaly Detection",
            "description": "AI fraud detection project"
        }
    ]

    return Response(data)


@api_view(['GET'])
def qualifications(request):
    data = [
        "Bachelor Degree in Data Science",
        "Django Web Development",
        "Machine Learning Knowledge"
    ]

    return Response(data)