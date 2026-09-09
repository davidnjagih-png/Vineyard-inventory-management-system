# SETUP
Clone repository  
in terminal run:
   -pipenv install  
   -pipenv shell

# REQUIREMENTS

# Users file

- create a login portal with authentication and user management features.
- the portal should allow users to login based on their credentials and access different features based on their roles.
- The portal should include the following functionalities:
  - user login and logout (based on hardcoded credentials)
  - user profile:
    - admin: can add new wine batches (record type, vintage, quantity)
    - manager: can track stock levels (table grapes and wine grapes quantity and quality)
    - sales team view sales projections and price wine and table grapes
    - owner view a dashboard summary and create new user accounts with specific roles (admin, manager, sales team)
  - user registration (with role selection)(to be accessible only by the owner)

# wine batch management:

- Admin can add new wine batches with details such as record type, vintage, and quantity.
- Admin can edit or delete existing wine batches.
- sales team can view wine batches and their details but cannot modify them.
- sales team can also view sales projections and price wine based on the available stock.
- Owner can view all wine batches and their details.
- set the type to be of three categories: red, white, and rose.
- add a feature to calculate the estimated wine production (in litres) based on the quantity of grapes and the type of wine batch.
- 1.5kg of wine grapes = 1 Litre of wine
- 750ml of wine = 1 bottle of wine

# grape stock management:

- Manager can track stock levels of table grapes and wine grapes, including quantity and quality.
- Manager can update stock levels as needed. - Sales team can view stock levels but cannot modify them.
- sales team can also view sales projections and price table grapes based on the available stock.
- set the type to be of two categories: table grapes and wine grapes.
- wine grapes should be linked to wine batches for production tracking.
- wine grapes should show the quantity of the types of wine grape varieties (i.e., red, white, and rose)
- set a feature to estimate the total number of table grape packets from the available stock based on the average weight of a packet and the total quantity of table grapes in stock.
- 1 kg of table grapes = 2 packets (average weight of a packet is 500g)

# sales projections:

- Sales team can view sales projections for both wine and table grapes.
- Sales team can price wine and table grapes based on current stock levels and market trends.
- Sales team can generate reports on sales performance and projections.
- the team can price wine based on the type of wine batch (red, white, or rose) and the quantity available in stock.
- the sales team can price table grapes based on the quantity available in stock and the average market price per packet.

# inventory management logic:

- The system should maintain an inventory of wine batches and grape stock levels.
- Inventory levels should be updated in real- time based on sales and stock updates.
- The system should provide alerts for low stock levels and allow managers to reorder as necessary.
- The system should generate reports on inventory status, including current stock levels, sales performance, and projections.

# forecasting logic:

- The system should include forecasting logic to predict future sales and stock requirements based on historical data and market trends.
- The forecasting model should take into account seasonal variations, market demand, and other relevant factors.
- The system should provide recommendations for inventory management based on the forecasted data.

# cli interface:

- The portal should have a command- line interface (CLI) for users to interact with the system.
- The CLI should provide clear instructions and prompts for users to perform various actions based on their roles.
- The CLI should include error handling and validation to ensure smooth user experience.
- should include inputs for the following functionalities:
  - user login and logout
  - user profile management
  - wine batch management (add, edit, delete, view)
  - grape stock management (track, update, view)
  - sales projections and pricing - inventory management and reporting
  - forecasting and recommendations - user registration (for owner role only)

# main.py:

- The main entry point of the application, which initializes the CLI and handles user authentication.
- The main.py file should include logic to route users to their respective functionalities based on their roles.
- It should also handle user registration for the owner role and manage user sessions.

# tests:

- The application should include unit tests to verify the functionality of each component.
- Tests should cover user authentication, role- based access control, inventory management, sales projections, and forecasting logic.
- The tests should ensure that the system behaves as expected under various scenarios and edge cases.
