# Forked from https://github.com/ayush-git228/StockStitch

# StockStitch

StockStitch is a business management web application built with Django. It provides comprehensive tools for managing customers, orders, inventory, requirements, payments, and more, with a focus on usability and professional design.

## Key Features
- **Meeting Mode:** Quick entry for customers, orders, requirements, and payments in a single form.
- **Requirements Tracking:** Track steps done and steps not done for each requirement, with live checklist and dynamic counters.
- **Import/Export:** Bulk import and export of data (CSV/Excel) for all major models, with sample files and error reporting.
- **Inventory & Orders:** Manage inventory items, suppliers, purchases, and customer orders with detailed forms and analytics.
- **Audit Log:** Track changes to all major models.
- **API Access:** REST API for integration.
- **Modern UI:** Responsive, professional design with Bootstrap and custom SCSS.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd StockStitch
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage Notes
- Access Meeting Mode from the navigation bar for rapid data entry.
- Use the Requirements section to manage fulfillment steps with live checklists.
- Import/export data from the respective model pages using the provided forms and sample CSVs.
- All changes are tracked in the audit log for transparency.

## More
- Need to implement something like WebRTC for enabling real-time communication (like audio and video) 
  directly between browsers and devices
