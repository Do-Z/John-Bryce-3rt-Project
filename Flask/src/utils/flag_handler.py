class FlagHandler:
    # initiating array of countries and flag icons based on bootstrap classes
    @staticmethod
    def get_countries_with_flags_classes():
        countries_with_flags_classes = [
            ('USA', 'flag-icon-us'),
            ('Germany', 'flag-icon-de'),
            ('Spain', 'flag-icon-es'),
            ('United Kingdom', 'flag-icon-gb'),
            ('India', 'flag-icon-in'),
            ('Brazil', 'flag-icon-br'),
            ('Italy', 'flag-icon-it'),
            ('Georgia', 'flag-icon-ge'),
            ('Turkey', 'flag-icon-tr'),
            ('Sweden', 'flag-icon-se'),
            ('France', 'flag-icon-fr')
        ]
        return countries_with_flags_classes
    