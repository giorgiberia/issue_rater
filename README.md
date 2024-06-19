# Issues Voting App

This is a Django-based web application for tracking issues and allowing users to vote on them. The app provides functionality for creating new issues and voting on existing issues with upvotes and downvotes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Files](#key-files)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Pipenv or virtualenv for managing dependencies

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/issues-voting-app.git
    cd issues-voting-app
    ```

2. Create a virtual environment:

    ```bash
    pipenv install
    pipenv shell
    ```

    Or with virtualenv:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Usage

- To create a new issue, fill in the form on the right side of the page and click "Save".
- To vote on an issue, click the "Upvote" or "Downvote" buttons next to the issue in the list.

## Project Structure

- `issues/`: Main app directory
  - `migrations/`: Database migrations for the app
  - `static/`: Static files (CSS, JavaScript, images)
  - `templates/`: HTML templates
  - `admin.py`: Admin configuration for the app
  - `apps.py`: App configuration
  - `forms.py`: Forms used in the app
  - `models.py`: Database models
  - `tests.py`: Test cases
  - `urls.py`: URL routing for the app
  - `views.py`: View functions

- `project/`: Project-level configuration
  - `settings.py`: Django settings
  - `urls.py`: URL routing for the project
  - `wsgi.py`: WSGI configuration

- `manage.py`: Django's command-line utility

## Key Files

### `issues/models.py`

Defines the database models for the app:

- `Issue`: Model representing an issue.
- `Vote`: Model representing a vote on an issue.

### `issues/forms.py`

Defines the forms used in the app:

- `IssueForm`: Form for creating a new issue.
- `VoteForm`: Form for voting on an issue.

### `issues/views.py`

Contains the view functions for the app:

- `issue_list_and_create`: View for displaying the list of issues and creating a new issue.
- `vote_issue`: View for voting on an issue.

### `issues/templates/issues/issue_list_and_create.html`

HTML template for displaying the list of issues and the form for creating a new issue.

### `issues/static/css/styles.css`

CSS file for styling the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any changes.

## License

This project is licensed under the MIT License.
