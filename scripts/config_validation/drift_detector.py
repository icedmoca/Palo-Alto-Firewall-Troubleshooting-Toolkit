from deepdiff import DeepDiff
import hashlib
import json
from datetime import datetime

class ConfigDriftDetector:
    def __init__(self):
        self.baseline_configs = {}
        self.drift_history = []
        
    def compute_config_hash(self, config):
        config_str = json.dumps(config, sort_keys=True)
        return hashlib.sha256(config_str.encode()).hexdigest()
    
    def set_baseline(self, config_type, config):
        self.baseline_configs[config_type] = {
            'config': config,
            'hash': self.compute_config_hash(config),
            'timestamp': datetime.now()
        }
    
    def detect_drift(self, config_type, current_config):
        if config_type not in self.baseline_configs:
            raise ValueError(f"No baseline set for {config_type}")
            
        baseline = self.baseline_configs[config_type]['config']
        diff = DeepDiff(baseline, current_config, ignore_order=True)
        
        if diff:
            drift_event = {
                'timestamp': datetime.now(),
                'config_type': config_type,
                'changes': diff.to_dict(),
                'severity': self._calculate_drift_severity(diff)
            }
            self.drift_history.append(drift_event)
            return drift_event
        return None
    
    def _calculate_drift_severity(self, diff):
        # Implement severity calculation based on change types
        severity_scores = {
            'dictionary_item_added': 5,
            'dictionary_item_removed': 8,
            'values_changed': 3,
            'type_changes': 10
        }
        total_score = sum(
            severity_scores.get(change_type, 1) * len(changes)
            for change_type, changes in diff.to_dict().items()
        )
        return 'HIGH' if total_score > 20 else 'MEDIUM' if total_score > 10 else 'LOW' 