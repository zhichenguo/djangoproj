# djangoproj
Prototype REST API in Python Django

<p>First, download this repository or pull this repository to your local machine:</p>
<pre><code>git clone https://github.com/zhichenguo/djangoproj.git</code></pre>

<p>Recommend Python version 3.8. </p>
<p>To create a new environment simply run:</p>
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

<p>Login with the superuser <code>username:john    password:John123456</code> to test the database structures.</p>
<p>Or, login with one of the un-superuser <code>username:bill    password:Bill123456</code> and <code>username:chris    password:Chris123456</code> to test the features of the API views.</p>

<p><a href="http://127.0.0.1:8000/question/">http://127.0.0.1:8000/question/</a> to test question API view </p>
<p><a href="http://127.0.0.1:8000/answer/">http://127.0.0.1:8000/answer/</a> to test answer API view </p>
<p><a href="http://127.0.0.1:8000/questionbookmark/">http://127.0.0.1:8000/questionbookmark/</a> to test question bookmark API view </p>
<p><a href="http://127.0.0.1:8000/answerbookmark/">http://127.0.0.1:8000/answerbookmark/</a> to test answer bookmark API view </p>
<p>The un-superusers only can see their own bookmarks.</p>


