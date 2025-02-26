from typing import Dict, List, Tuple
import pandas as pd
import numpy as np
from scipy import signal, stats
from statsmodels.tsa.seasonal import seasonal_decompose
from datetime import datetime, timedelta
import networkx as nx
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class TrafficPattern:
    pattern_id: str
    start_time: datetime
    end_time: datetime
    source_ips: List[str]
    destination_ips: List[str]
    protocols: Dict[str, int]
    ports: Dict[int, int]
    bytes_transferred: int
    packet_count: int
    average_packet_size: float
    risk_score: float

class TrafficPatternAnalyzer:
    def __init__(self):
        self.patterns = {}
        self.baseline_metrics = defaultdict(list)
        self.anomaly_thresholds = {
            'volume': 2.5,  # Standard deviations from mean
            'entropy': 0.7,  # Normalized entropy threshold
            'burst_factor': 3.0  # Sudden traffic increase factor
        }
        
    def analyze_traffic(self, traffic_data: pd.DataFrame, window_size: str = '1H') -> Dict:
        """
        Comprehensive traffic analysis with multiple detection methods
        """
        results = {
            'temporal_patterns': self._analyze_temporal_patterns(traffic_data, window_size),
            'spatial_patterns': self._analyze_spatial_patterns(traffic_data),
            'protocol_analysis': self._analyze_protocol_distribution(traffic_data),
            'anomalies': self._detect_anomalies(traffic_data),
            'risk_assessment': self._assess_traffic_risk(traffic_data)
        }
        
        # Correlate findings across different analyses
        results['correlated_findings'] = self._correlate_findings(results)
        return results

    def _analyze_temporal_patterns(self, data: pd.DataFrame, window_size: str) -> Dict:
        """Analyze temporal aspects of traffic patterns"""
        # Resample data to regular intervals
        resampled = data.resample(window_size).agg({
            'bytes': 'sum',
            'packets': 'count',
            'source_ip': 'nunique',
            'dest_ip': 'nunique'
        })
        
        # Perform seasonal decomposition
        decomposition = seasonal_decompose(
            resampled['bytes'],
            period=self._detect_seasonality(resampled['bytes'])
        )
        
        # Detect bursts using wavelet transform
        bursts = self._detect_traffic_bursts(resampled['bytes'])
        
        return {
            'trend': decomposition.trend.to_dict(),
            'seasonal': decomposition.seasonal.to_dict(),
            'bursts': bursts,
            'daily_patterns': self._extract_daily_patterns(resampled),
            'weekly_patterns': self._extract_weekly_patterns(resampled)
        }

    def _analyze_spatial_patterns(self, data: pd.DataFrame) -> Dict:
        """Analyze spatial distribution of traffic"""
        # Create traffic flow graph
        flow_graph = nx.DiGraph()
        
        # Aggregate flows between IP pairs
        flows = data.groupby(['source_ip', 'dest_ip']).agg({
            'bytes': 'sum',
            'packets': 'count'
        }).reset_index()
        
        # Add nodes and edges to graph
        for _, flow in flows.iterrows():
            flow_graph.add_edge(
                flow['source_ip'],
                flow['dest_ip'],
                weight=flow['bytes'],
                packets=flow['packets']
            )
        
        # Calculate network metrics
        return {
            'centrality': nx.degree_centrality(flow_graph),
            'communities': self._detect_communities(flow_graph),
            'flow_patterns': self._analyze_flow_patterns(flow_graph),
            'hotspots': self._identify_traffic_hotspots(flow_graph)
        }

    def _detect_communities(self, graph: nx.DiGraph) -> Dict:
        """Detect communities in traffic flow"""
        communities = nx.community.greedy_modularity_communities(graph.to_undirected())
        return {
            f'community_{i}': list(community)
            for i, community in enumerate(communities)
        }

    def _analyze_protocol_distribution(self, data: pd.DataFrame) -> Dict:
        """Analyze protocol usage patterns"""
        protocol_stats = data.groupby('protocol').agg({
            'bytes': ['sum', 'mean', 'std'],
            'packets': ['count', 'mean', 'std']
        }).to_dict()
        
        # Calculate protocol entropy
        protocol_counts = data['protocol'].value_counts()
        protocol_entropy = stats.entropy(protocol_counts)
        
        return {
            'statistics': protocol_stats,
            'entropy': protocol_entropy,
            'unusual_combinations': self._detect_unusual_protocol_combinations(data)
        }

    def _detect_anomalies(self, data: pd.DataFrame) -> List[Dict]:
        """Detect various types of traffic anomalies"""
        anomalies = []
        
        # Volume-based anomalies
        volume_anomalies = self._detect_volume_anomalies(data)
        if volume_anomalies:
            anomalies.extend(volume_anomalies)
        
        # Pattern-based anomalies
        pattern_anomalies = self._detect_pattern_anomalies(data)
        if pattern_anomalies:
            anomalies.extend(pattern_anomalies)
        
        # Protocol anomalies
        protocol_anomalies = self._detect_protocol_anomalies(data)
        if protocol_anomalies:
            anomalies.extend(protocol_anomalies)
        
        return anomalies

    def _assess_traffic_risk(self, data: pd.DataFrame) -> Dict:
        """Assess risk levels in traffic patterns"""
        return {
            'overall_risk_score': self._calculate_risk_score(data),
            'risk_factors': self._identify_risk_factors(data),
            'recommendations': self._generate_risk_recommendations(data)
        }

    def _correlate_findings(self, results: Dict) -> List[Dict]:
        """Correlate findings across different analysis methods"""
        correlated_findings = []
        
        # Correlate temporal and spatial patterns
        temporal_spatial_correlation = self._correlate_temporal_spatial(
            results['temporal_patterns'],
            results['spatial_patterns']
        )
        if temporal_spatial_correlation:
            correlated_findings.extend(temporal_spatial_correlation)
        
        # Correlate anomalies with protocol analysis
        anomaly_protocol_correlation = self._correlate_anomalies_protocols(
            results['anomalies'],
            results['protocol_analysis']
        )
        if anomaly_protocol_correlation:
            correlated_findings.extend(anomaly_protocol_correlation)
        
        return correlated_findings

    def _detect_seasonality(self, series: pd.Series) -> int:
        """Detect the dominant seasonality period"""
        # Implementation using FFT or autocorrelation
        return 24  # Default to daily seasonality

    def _detect_traffic_bursts(self, series: pd.Series) -> List[Dict]:
        """Detect sudden traffic bursts"""
        # Implementation using wavelet transform or rolling statistics
        return []

    def _extract_daily_patterns(self, data: pd.DataFrame) -> Dict:
        """Extract daily traffic patterns"""
        return {}

    def _extract_weekly_patterns(self, data: pd.DataFrame) -> Dict:
        """Extract weekly traffic patterns"""
        return {} 