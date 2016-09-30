import unittest 
from unittest import TestCase
from model import db, example_data, connect_to_db
from server import app 
import server 
from mock import MagicMock 


#################### DATABASE TESTING ####################
class GrowshareDatabase(TestCase):
    def setUp(self):
        """ Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True 
        # Connect to test database
        connect_to_db(app, 'postgresql:///growshare_test')

        # Create tables and add sample data 
        db.drop_all()
        db.create_all()
        example_data() 
        print "settup successful"

    def tearDown(self):
        """ Do at the end of every test."""

        db.session.close() 
        db.drop_all() 

        print "teardown successful"

#################### FLASK LOGGED IN TESTING ###############
class FlaskTestsLoggedIn(TestCase):
    """ Flask tests with user logged in to session."""

    def setUp(self):
        """ To do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

        self.client = app.test_client()
        connect_to_db(app, 'postgresql:///growshare_test')

        # Create tables and add sample data 
        db.drop_all()
        db.create_all()
        example_data() 
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1 

    def test_dashboard(self):
        """ Test dashboard page."""

        result = self.client.get("/dashboard")
        self.assertIn('Results', result.data)
        self.assertNotIn("Login", result.data)
        self.assertNotIn("Register", result.data)

    def test_landing_page(self):
        """ Test landing page."""

        result = self.client.get("/")
        self.assertIn("Dashboard", result.data)
        self.assertNotIn("Login", result.data)
        self.assertNotIn("Register", result.data)

    def test_logout(self):
        """ Test logout. """

        result = self.client.get('/logout', follow_redirects=True)
        self.assertIn('Logged out.', result.data)

############### FLASK LOGGED OUT TESTING ####################
class LoggedOut(TestCase):

    def setUp(self):
        """ To do before every test."""

        app.config['TESTING'] = True 
        self.client = app.test_client() 

    def test_dashboard(self):
        """ Test dashboard page."""

        result = self.client.get("/dashboard")
        self.assertIn("Login", result.data)
        self.assertIn("Register", result.data)
        self.assertNotIn("Results", result.data)

    def test_landing_page(self):
        """ Test landing page."""

        result = self.client.get("/")
        self.assertIn("Login", result.data)
        self.assertIn("Register", result.data)
        self.assertNotIn("Dashboard", result.data)

##################### FLASK ROUTE TESTS ####################
class FlaskTests(TestCase):

    def setUp(self):
        """ To do before every test."""

        self.client = app.test_client() 
        app.config['TESTING'] = True 

    def test_signup_logout_flask_route(self):
        """ Non-database test. """

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h4>Grow what you <i>love</i>. Share what you <i>grow</i>.</h4>', result.data)


    def tearDown(self):
        print "(tearDown ran)"

##################### APP INTEGRATION TESTS ####################
class MyAppIntegrationTestCase(TestCase):

    def setUp(self):
        """ To do before. """

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True 
        server.app.config['DEBUG'] = False 

    def test_landing_page(self):
        test_client = server.app.test_client()
        result = test_client.get('/')
        self.assertIn('<h4>Grow what you <i>love</i>. Share what you <i>grow</i>.</h4>', result.data)

    def test_dashboard_page(self):
        test_client = server.app.test_client()
        result = test_client.get('/dashboard')
        self.assertIn('<center><div class="panel-title"><i>Results</i></div></center>', result.data)

    def tearDown(self):
        print "(tearDown ran)"


################################################################################

if __name__ == "__main__":
    unittest.main()



















