def calculate_wood_price(density, length, width, height, price_per_cubic_meter):
    """
    Calculate the price of wood based on density, dimensions, and price per cubic meter.
    Args:
        density (float): Density of wood in kg/m³.
        length (float): Length of the wood in meters.
        width (float): Width of the wood in meters.
        height (float): Height of the wood in meters.
        price_per_cubic_meter (float): Price per cubic meter of the wood.

    Returns:
        tuple: Price, Volume, and Mass of the wood.
    """
    volume = length * width * height  # Volume in cubic meters
    mass = density * volume  # Mass in kg
    price = price_per_cubic_meter * volume  # Price in local currency
    return price, volume, mass
