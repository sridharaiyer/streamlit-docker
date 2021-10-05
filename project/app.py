import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass
# Custom imports
from multipage import MultiPage
from pages import penguins, session_state, stock_SP500, boston_housing
from pages import home

# Create an instance of the app
app = MultiPage()

# Add all your application here
app.add_page("Home", home.app)
app.add_page("Session State Demos", session_state.app)
app.add_page("Penguins", penguins.app)
app.add_page("Stocks S&P 500", stock_SP500.app)
app.add_page("Boston Housing - Random Forest Regressor", boston_housing.app)

# The main app
app.run()
