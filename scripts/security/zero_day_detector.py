import numpy as np
from sklearn.ensemble import IsolationForest
from scipy.stats import entropy
from collections import defaultdict

class ZeroDayDetector:
    def __init__(self):
        self.isolation_forest = IsolationForest(
            contamination=0.01,  # Expected proportion of anomalies
            random_state=42
        )
        self.behavior_baseline = defaultdict(list)
        self.entropy_thresholds = {}
        
    def build_behavioral_baseline(self, normal_traffic_data):
        """Build baseline of normal network behavior patterns"""
        for traffic in normal_traffic_data:
            features = self._extract_behavioral_features(traffic)
            for feature_name, value in features.items():
                self.behavior_baseline[feature_name].append(value)
        
        # Calculate entropy thresholds for each feature
        for feature_name, values in self.behavior_baseline.items():
            self.entropy_thresholds[feature_name] = self._calculate_entropy_threshold(values)
    
    def _extract_behavioral_features(self, traffic_data):
        """Extract sophisticated behavioral features from traffic"""
        return {
            'protocol_distribution': self._calculate_protocol_entropy(traffic_data),
            'port_usage_pattern': self._analyze_port_usage(traffic_data),
            'payload_characteristics': self._analyze_payload(traffic_data),
            'temporal_pattern': self._analyze_temporal_behavior(traffic_data)
        }
    
    def detect_anomalous_behavior(self, current_traffic):
        features = self._extract_behavioral_features(current_traffic)
        anomaly_scores = {}
        
        for feature_name, value in features.items():
            baseline_entropy = entropy(self.behavior_baseline[feature_name])
            current_entropy = entropy([value])
            
            deviation = abs(current_entropy - baseline_entropy)
            anomaly_scores[feature_name] = deviation > self.entropy_thresholds[feature_name]
        
        return self._evaluate_anomaly_significance(anomaly_scores) 