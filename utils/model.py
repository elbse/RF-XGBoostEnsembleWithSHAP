import random
import hashlib

class ThreatModel:
    """Simulated ML model for threat detection"""
    
    def __init__(self):
        self.model_type = "Ensemble (RF + XGBoost)"
        self.features = [
            'SEND_SMS', 'READ_CONTACTS', 'GET_DEVICE_ID', 'SEND_TEXT_MESSAGE',
            'INTERNET', 'CAMERA', 'RECORD_AUDIO', 'ACCESS_FINE_LOCATION',
            'READ_PHONE_STATE', 'INSTALL_PACKAGES', 'WRITE_EXTERNAL_STORAGE'
        ]
    
    def predict(self, file_hash):
        """Predict if file is malware based on hash"""
        # Seed with file hash for consistent results
        seed = int(file_hash[:8], 16) if len(file_hash) >= 8 else hash(file_hash)
        random.seed(seed)
        
        threat_score = random.uniform(0, 1)
        is_malware = threat_score > 0.65
        
        # Generate feature contributions
        contributions = {}
        for feature in self.features:
            base = random.uniform(-0.3, 0.5)
            if is_malware:
                base = abs(base) * 1.5
            contributions[feature] = base
        
        return {
            'threat_score': threat_score,
            'is_malware': is_malware,
            'confidence': random.uniform(0.85, 0.99),
            'contributions': contributions,
            'suspicious_features': [f for f in self.features if contributions.get(f, 0) > 0.2][:5]
        }

# Global model instance
_model = None

def get_model():
    """Get or create model instance"""
    global _model
    if _model is None:
        _model = ThreatModel()
    return _model

def get_prediction(file_hash):
    """Get prediction for a file hash"""
    model = get_model()
    return model.predict(file_hash)