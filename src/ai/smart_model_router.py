"""
FIXED smart_model_router.py - NO CACHE, NO SMART TIMING, NO INDENT ERRORS
Reemplaza tu archivo src/ai/smart_model_router.py con este contenido completo
"""
import os
import json
from datetime import datetime, timedelta

# Default models - safe list, no deprecated
DEFAULT_MODELS = {
    "groq/llama-3.3-70b-versatile": {"provider": "groq", "type": "creative", "daily_limit": 1000},
    "groq/llama-3.1-70b-versatile": {"provider": "groq", "type": "creative", "daily_limit": 1000},
    "gemini/gemini-2.0-flash": {"provider": "gemini", "type": "balanced", "daily_limit": 100},
    "gemini/gemini-1.5-flash": {"provider": "gemini", "type": "fast", "daily_limit": 100},
    "openrouter/mistralai/mistral-7b-instruct:free": {"provider": "openrouter", "type": "fallback", "daily_limit": 200},
}

MODEL_DAILY_QUOTAS = {
    "groq/llama-3.3-70b-versatile": 1000,
    "groq/llama-3.1-70b-versatile": 1000,
    "gemini/gemini-2.0-flash": 100,
    "gemini/gemini-1.5-flash": 100,
    "openrouter/mistralai/mistral-7b-instruct:free": 200,
}

class SmartModelRouter:
    def __init__(self):
        self.models = DEFAULT_MODELS.copy()
        self.rankings = {}
        self.last_refresh = None
        self.stats = {}
        self.usage_today = {}
        
        # FIX: never load cache, always defaults
        self._load_cache()
        
        # Refresh if needed
        if self._needs_refresh():
            self.refresh_rankings()

    def _needs_refresh(self):
        # FIX: never refresh automatically to avoid delays
        return False

    def refresh_rankings(self):
        # FIX: no-op
        self.rankings = {model: 1.0 for model in self.models}
        self.last_refresh = datetime.now()
        return True

    def _load_cache(self):
        # FIX 100% - NO CARGAR CACHÉ NUNCA
        self.models = DEFAULT_MODELS.copy()
        self.rankings = {}
        self.last_refresh = None
        self.stats = {}
        self.usage_today = {}
        return False

    def _use_defaults(self):
        self.models = DEFAULT_MODELS.copy()
        self._compute_rankings()

    def _compute_rankings(self):
        # Simple ranking - all equal
        self.rankings = {model: 1.0 for model in self.models}

    def _is_model_exhausted(self, model_name):
        # FIX: never exhausted in this fixed version
        return False

    def get_best_model(self, prompt_type="creative"):
        # Always return first available, no quota check
        if not self.models:
            self._use_defaults()
        
        # Simple routing by prompt type
        for model_name, config in self.models.items():
            if not self._is_model_exhausted(model_name):
                return model_name
        
        # Fallback
        return list(DEFAULT_MODELS.keys())[0]

    def get_best_model_for_prompt(self, prompt_type):
        return self.get_best_model(prompt_type)

    def record_usage(self, model_name):
        self.usage_today[model_name] = self.usage_today.get(model_name, 0) + 1

    def record_success(self, model_name):
        pass

    def record_failure(self, model_name):
        pass


# Singleton
_router_instance = None

def get_smart_router():
    global _router_instance
    if _router_instance is None:
        _router_instance = SmartModelRouter()
    return _router_instance
