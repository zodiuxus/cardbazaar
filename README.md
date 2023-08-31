# Card Bazaar
Welcome to Card Bazaar, a trading market for cards designed for use within the Balkan region.

The platform allows people to sell, and buy from cards among each other. 

On principle, the system is designed to be simple and usable by everyone, allowing even the inexperienced to get in on the trading aspect of trading card games.

Planned features:
- Ordering
- Messaging
- Price trends
- Card search

The system at the moment is lackluster in features, however more will be added as time goes on. At some point, this repository will be made private - or deleted, to protect my work.

---

By default, the project only comes with the models, not with the database. First you will need to naviage to the directory and execute  `python manage.py migrate`, followed by `python manage.py migrate --run-syncdb`.

To use it, first you'll need to create a superuser (with all the relevant fields) with `python manage.py createsuperuser`.

Finally, to run the project, execute `python manage.py runserver`.

The project is setup in a way that when a person creates an account on the website, they will have to choose between creating a Seller, or a Buyer account. If you want your superuser to have the properties of both (they are not mutually exclusive), you will have to add new Seller and Buyer accounts and connect them to the superuser from the admin page. Otherwise, users can go through the basic user creation forms as usual.

To add a card, you will need to use a seller account, go to your profile, and press the `Add card?` button. Unfortunately, due to some issues with the way the form is made (using an inline_formset), it instantiates more than 1 form, and you can't fill them, as it always will return an error that the fields are required, even when the fields are filled. For now, to add a card, you will need to go to the admin page, and look for `SellerCardDetail`, where you can add them. You can see that there are more fields there than there are on the regular form.

Some of the data there will be automatically filled from the `CardData` model, as commented in the `views.py` file. The data is taken from Scryfall, and you can fill that table by importing data from their bulk flies. See https://scryfall.com/docs/api/bulk-data. The data is taken from the `Default Cards` file.

The 30 most recent cards are rendered on the main page, along with their name, price, current seller stock, the seller's name, and their reputation.
