from gpcp_data import get_precip_monthly_mean, show_bar_chart

if __name__ == '__main__':
    """
    Google Gemini:
    Chennai's heaviest one-day rainfall in history was 494 mm (19.45 inches), 
    recorded on December 1, 2015, during the catastrophic 2015 South India floods.
    """
    precip  = get_precip_monthly_mean()

    lat_long = (13.07096267632839, 80.28562580980238) # Chennai, India
    years = [2015, 2016]

    lat_long = (35.77004795786844, -82.1950845636907) # Busick, NC, USA
    years = [2018, 2019]

    show_bar_chart(precip, lat_long, years)
