"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        'stock.jinja2',
        title='StockApp',
        template='stock-template',
        current_user=current_user
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))