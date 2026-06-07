import json
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def analyze_scope(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            client_text = data.get('text', '').lower()
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)

        modules = []
        total_hours = 0
        
        # Rule 1: Security & Authentication
        if re.search(r'\b(login|secure|auth|profile|users|passwords)\b', client_text):
            modules.append({
                "category": "SECURITY", 
                "title": "Authentication Engine", 
                "stack": "Django Auth + JWT", 
                "hours": 25
            })
            total_hours += 25
            
        # Rule 2: Commerce & Transactions
        if re.search(r'\b(store|pay|checkout|cart|stripe|e-commerce|commerce)\b', client_text):
            modules.append({
                "category": "TRANSACTIONAL", 
                "title": "E-Commerce Gateway", 
                "stack": "Stripe API + PostgreSQL", 
                "hours": 40
            })
            total_hours += 40

        # Rule 3: Data & Dashboards
        if re.search(r'\b(dashboard|charts|analytics|metrics|data)\b', client_text):
            modules.append({
                "category": "VISUALIZATION", 
                "title": "Data Visualization", 
                "stack": "React + Recharts", 
                "hours": 35
            })
            total_hours += 35
# Rule 4: Artificial Intelligence & Chatbots
        if re.search(r'\b(ai|chatbot|bot|llm|openai|nlp|machine learning)\b', client_text):
            modules.append({
                "category": "INTELLIGENCE", 
                "title": "LLM Chatbot Engine", 
                "stack": "Python + LangChain + OpenAI", 
                "hours": 50
            })
            total_hours += 50
            
        # Rule 5: Recommendation Algorithms
        if re.search(r'\b(recommend|personality|style|taste|outfit|algorithm)\b', client_text):
            modules.append({
                "category": "ALGORITHM", 
                "title": "Style Recommendation Matrix", 
                "stack": "Scikit-Learn + Vector DB", 
                "hours": 45
            })
            total_hours += 45
        # Base Project Architecture (Overhead)
        base_hours = 20
        total_hours += base_hours

        return JsonResponse({
            "total_hours": total_hours,
            "complexity_score": len(modules) * 2.5,
            "modules": modules
        })
        
    return JsonResponse({"error": "Method not allowed. Use POST."}, status=405)