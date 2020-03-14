# djangoproj
Prototype REST API in Python Django

<p>First, download this repository or pull this repository to your local machine:</p>
<pre><code>git clone https://github.com/zhichenguo/djangoproj.git</code></pre>

<p>Recommend Python version 3.8. To create a new environment simply run:</p>
<pre><code>conda create --name dj_env python=3.8 -y</code></pre>
<p>Once it's created, then activate it by running:</p>
<pre><code>conda activate dj_env</code></pre>

<p>Please navigate to <code>djangoproj/</code> directory, then run the following commands to install all the package required:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<p>Run the following commands to start the Django development server:</p>
<pre><code>python manage.py runserver</code></pre>

<p>Please create a new terminal and navigate to <code>djangoproj/restapiproj/</code> directory, then run the following commands for testing:</p>
<pre><code>python manage.py test</code></pre>

<p>Alternatively, the Django site can be assessed via <a href="http://127.0.0.1:8000/admin/login/?next=/admin/" rel="nofollow">http://127.0.0.1:8000/admin/login/?next=/admin/</a> with any browser to test the features directly: </p>
<p>
<p>Login with the superuser <code>username: john  password: John123456</code> to test the database.</p>
<p>Or, login with one of the un-superuser <code>username: bill  password: Bill123456</code> and <code>username: chris  password: Chris123456</code> to test the features of the API views.</p>


