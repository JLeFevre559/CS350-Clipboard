# AI Prompts - Code - Milestone 5 - Shane Loewe

## Note that I utilized ChatGPT a lot in figuring out the edit profile functionality. I only included a sample of the type of questions I was giving it

### I think my problem is that I'm not passing the user ID correctly. In my database, the user ID is saved under the attribute "_id", an example of the data in this field is ObjectId('6536d000c66b4357290ddc74'). I'm guessing that I have to pass the user ID so it knows which user to update. But how do I pass this from the form to the view? 

If your user IDs are stored in your database as `ObjectId` objects, typically associated with MongoDB, and you want to pass this ID from your form to the view in Django, you need to convert the `ObjectId` to a string or a format that can be recognized in Django.

You can convert the `ObjectId` to a string and include it as a hidden input field in your form. Here's how you can do it:

1. In your Django view, retrieve the user's `_id` and convert it to a string:

```python
from bson import ObjectId

# Assuming you have a user object
user = get_user_model().objects.get(...)  # Retrieve the user as needed
user_id_str = str(user._id)  # Convert ObjectId to a string
```

2. Pass `user_id_str` to your template, which will be used in the form.

3. In your HTML template, add a hidden input field to include the user ID:

```html
<form method="post" action="{% url 'update_profile' %}">
    {% csrf_token %}
    <!-- Add a hidden input field for the user ID -->
    <input type="hidden" name="user_id" value="{{ user_id_str }}">
    <!-- Editable fields (e.g., name, email, etc.) -->
    <input type="text" name="first_name" value="{{ user.first_name }}">
    <input type="text" name="last_name" value="{{ user.last_name }}">
    <input type="email" name="email" value="{{ user.email }}">
    <input type="text" name="bio" value="{{ user.bio }}">
    <input type="submit" value="Save">
</form>
```

4. In your view function, you can retrieve the user ID from the form data as follows:

```python
user_id = request.POST.get("user_id")
```

By including the user ID as a hidden input field in your form, it will be submitted along with the other form data, and you can use it in your view to identify the user whose profile you want to update.

### how would I change this code to capitalize the string: <h2 class="ProfileIcon" , id="profile-picture">{{ user.first_name.0|default:" " }}{{ user.last_name.0|default:" " }}</h2>

To capitalize the string within the `<h2>` element in your code, you can use Python's string methods to change the text to uppercase or title case (capitalizing the first letter of each word). You can achieve this by modifying the template tag in the Django template. Here's how you can do it:

1. To capitalize the entire string (convert it to uppercase), you can use the `upper` filter:

```html
<h2 class="ProfileIcon" id="profile-picture">
    {{ user.first_name.0|default:" " }}{{ user.last_name.0|default:" "|upper }}
</h2>
```

2. To capitalize the first letter of each word in the string (title case), you can use the `title` filter:

```html
<h2 class="ProfileIcon" id="profile-picture">
    {{ user.first_name.0|default:" "|title }}{{ user.last_name.0|default:" "|title }}
</h2>
```

Choose the one that best suits your needs. The `upper` filter will convert the entire string to uppercase, while the `title` filter will capitalize the first letter of each word.