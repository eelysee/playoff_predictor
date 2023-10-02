import nba_apiv3.stats.endpoints as ep


class DeferredEndpoint:
    '''Simple class to represent an endpoint with deferred evaluation.'''
    def __init__(self, endpoint_class, **kwargs):
        self.endpoint_class = endpoint_class
        self.kwargs = kwargs

    def __call__(self):
        return self.endpoint_class(**self.kwargs)


# A bunch of valid but uninstantiated endpoints for testing:
deferred_endpoints = [
    DeferredEndpoint(ep.BoxScoreAdvancedV3, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScoreDefensiveV2, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScoreFourFactorsV3, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScoreMatchupsV3, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScoreMiscV3, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScorePlayerTrackV3, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScoreScoringV3, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScoreTraditionalV3, game_id='0021700807'),
    DeferredEndpoint(ep.BoxScoreUsageV3, game_id='0021700807'),
    DeferredEndpoint(ep.PlayByPlayV3, game_id='0021700807'),
]
