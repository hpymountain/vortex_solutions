from tokeo.ext.appshare import app
from winterfell.core import consts
from winterfell.data_classes.user_class import User, read_user_list_from_db
from winterfell.data_classes.contract_class import Contract, get_all_contracts_in_db


ui = app.nicegui.ui
ux = app.nicegui.ux

@app.nicegui.fastapi_app.get('/api')
async def get_api():
    return {'msg': 'json api result'}

def getRows(user):
    if(user is None):
        return {}
    rows = [
        {'forename': user.forename, 'surname': user.surname, 'address': user.address, 'zipcode': user.zipcode, 'city': user.city, 'email': user.email}
    ]
    return rows

@ui.page('/show-users')
def show_users():
    ui.label('Show Accounts!').classes('text-2xl m-2')
    accountObjects: dict[str, User] = read_user_list_from_db()

    accounts = list()
    for account in accountObjects.keys():
        accounts.append(account)

    columns = [
        {'name': 'forename', 'label': 'forename', 'field': 'forename', 'required': True, 'align': 'left'},
        {'name': 'surname', 'label': 'surname', 'field': 'surname', 'sortable': True},
        {'name': 'address', 'label': 'address', 'field': 'address', 'sortable': True},
        {'name': 'zipcode', 'label': 'zipcode', 'field': 'zipcode', 'sortable': True},
        {'name': 'city', 'label': 'city', 'field': 'city', 'sortable': True},
        {'name': 'email', 'label': 'email', 'field': 'email', 'sortable': True}
    ]
    
    row = []

    def generate_user_buttons():
        with ui.column():
            ui.button('Delete User', on_click=lambda: accountObjects.get(user_selection.value).delete_in_db())        
            ui.button('Print Invoice', on_click=lambda: ui.navigate.to(f'/invoice/{user_selection.value}', new_tab=True))
            ui.button('Edit User', on_click=lambda: ui.navigate.to('/edit-user', new_tab=True))


    with ui.splitter() as splitter:
        with splitter.before:
            with ui.row():
                user_selection = ui.select(options=accounts, with_input=True)
                ok_button = ui.button('OK')
            ok_button.on('click', generate_user_buttons)
            ui.separator()
            ui.button('Delete Contract', on_click=lambda: ui.navigate.to('/delete-contract', new_tab=True))
            #ui.button('Add Contract', on_click=lambda: ui.notify("This function is not implemented yet :("))
            ui.button('Add Contract', on_click=lambda: ui.navigate.to('/add-contract', new_tab=True))
            ui.button('Add User', on_click=lambda: ui.navigate.to('/add-user', new_tab=True))

        with splitter.after:
            user_info_table = ui.table(columns=columns, rows=row, row_key='name')
            def updateRow():
                row = getRows(accountObjects.get(user_selection.value))
                user_info_table.rows = row
                user_info_table.update()
            ok_button.on('click', updateRow)

@ui.page('/edit-user')
def edit_user_layout():
    ui.label('Edit an User!').classes('text-2xl m-2')

    accountObjects: dict[str, User] = read_user_list_from_db()

    accounts = list()
    for account in accountObjects.keys():
        accounts.append(account)

    user_selection = ui.select(options=accounts, with_input=True)
    load_user_button = ui.button('Load User')

    surname = ui.input('Surname')
    forename = ui.input('Forename')
    address = ui.input('Address')
    zipcode = ui.input('Zipcode')
    city = ui.input('City')
    email = ui.input('Email')

    def edit_user():
        selected_user = accountObjects.get(user_selection.value)
        selected_user.surname = surname.value if surname.value != "" else selected_user.surname
        selected_user.forename = forename.value if forename.value != "" else selected_user.forename
        selected_user.address = address.value if address.value != "" else selected_user.address
        selected_user.zipcode = zipcode.value if zipcode.value != "" else selected_user.zipcode
        selected_user.city = city.value if city.value != "" else selected_user.city
        selected_user.email = email.value if email.value != "" else selected_user.email
        selected_user.update_in_db()
        ui.notify("User eddited!")

    def load_user():
        selected_user = accountObjects.get(user_selection.value)
        if selected_user is not None:
            surname.set_value(selected_user.surname)
            forename.set_value(selected_user.forename)
            address.set_value(selected_user.address)
            zipcode.set_value(selected_user.zipcode)
            city.set_value(selected_user.city)
            email.set_value(selected_user.email)
        
    button_ok = ui.button('OK', on_click = edit_user)
    button_ok.disable()
    load_user_button.on('click', lambda: (load_user(), button_ok.enable()))

@ui.page('/add-user')
def add_user_layout():
    ui.label('Add an User!').classes('text-2xl m-2')
    surname = ui.input('Surname')
    forename = ui.input('Forename')
    address = ui.input('Address')
    zipcode = ui.input('Zipcode')
    city = ui.input('City')
    email = ui.input('Email')

    user = User()
    def add_user():
        user.surname = surname.value
        user.forename = forename.value
        user.address = address.value
        user.zipcode = zipcode.value
        user.city = city.value
        user.email = email.value
        user.create_in_db()
        ui.notify("User added!")

    ui.button('OK', on_click = add_user)

@ui.page('/delete-contract')
def delete_contract():
    ui.label('Delete a contract!').classes('text-2xl m-2')

    accountObjects: dict[str, User] = read_user_list_from_db()
    contractObjects: dict[str, Contract] = read_user_list_from_db()

    accounts = list()
    for account in accountObjects.keys():
        accounts.append(account)

    user_selection = ui.select(options=accounts, with_input=True)

    def delete_contract(id):
        selected_contract = contractObjects.get(id)
        selected_contract.delete_in_db() if selected_contract is not None else ui.notify("Could not delete contract!")

    def generateUserContracts():
        selected_user = accountObjects.get(user_selection.value)
        contractObjects = selected_user.contracts
        user_contracts = list()
        for contract in contractObjects.keys():
            user_contracts.append(contract)
        contract_selection = ui.select(options=user_contracts, with_input=True)

        ui.button('OK', on_click = delete_contract(contract_selection.value))

    ui.button('Submit User', on_click = generateUserContracts)

@ui.page('/add-contract')
def add_contract_layout():
    ui.label('Add a Contract!').classes('text-2xl m-2')

    accountObjects: dict[str, User] = read_user_list_from_db()

    accounts = list()
    for account in accountObjects.keys():
        accounts.append(account)

    subscriptions = [
        'Green Mobile L', 'Green Mobile S', 'Green Mobile M'
    ]

    user_selection= ui.select(options=accounts, with_input=True)

    def create_contract(subscription, user):
        contract = Contract()
        if(subscription == 'Green Mobile S'):
            contract.basic_fee = 8
            contract.minutes_included = 0
            contract.price_per_extra_minute = 0.08
            contract.data_volume = 500000
        elif(subscription == 'Green Mobile M'):
            contract.basic_fee = 22
            contract.minutes_included = 100
            contract.price_per_extra_minute = 0.06
            contract.data_volume = 2000000
        elif(subscription == 'Green Mobile L'):
            contract.basic_fee = 42
            contract.minutes_included = 150
            contract.price_per_extra_minute = 0.04
            contract.data_volume = 5000000

        # contract.create_in_db()
        # user.contracts.update({id: contract})
        ui.notify("Contract cannot be created yet!")

    def add_contract():
        selected_user = accountObjects.get(user_selection.value)
        subscription_selection = ui.select(options=list(subscriptions), with_input=True)
        ui.button('Submit Subscription', on_click=create_contract(subscription_selection.value, selected_user))

    ui.button('Submit User', on_click=add_contract)


@ui.page('/show-services-trackings')
def show_users():
    ui.label('Show services trackings!').classes('text-2xl m-2')
    accounts = app.db.get_list('test_accounts', page=1, perPage=20, filter='', sort='created', cache=False)
    for account in accounts.items:
        with ux.ul().classes("divide-y divide-gray-100"):
            with ux.li().classes("flex justify-between gap-x-6 py-5"):
                with ux.div().classes("flex min-w-0 gap-x-4"):
                    ux.h2(f'{account.last_name}, {account.first_name}').classes("text-sm font-semibold leading-6 text-gray-900")
                    tracked = app.db.get_list('services_tracked', page=1, perPage=20, filter=f'account="{account.id}"', sort='created', cache=False)
                    for service in tracked.items:
                        with ux.div().classes("min-w-0 flex-auto"):
                            ux.p(service.service).classes("text-sm font-semibold leading-6 text-gray-900")
                            ux.p(f'{service.duration} min').classes("mt-1 truncate text-xs leading-5 text-gray-500")



@ui.page('/show-justus')
def show_justus():
    ui.label('Show Accounts!').classes('text-2xl m-2')
    # accounts = app.db.get_list('accounts', page=1, perPage=20, filter='', sort='created', cache=False)
    account = app.db.get_one('test_accounts', 'occ8e7xxas1i920')

    with ux.ul().classes("divide-y divide-gray-100"):
        with ux.li().classes("flex justify-between gap-x-6 py-5"):
            with ux.div().classes("flex min-w-0 gap-x-4"):
                with ux.div().classes("min-w-0 flex-auto"):
                    ux.p(account.last_name).classes("text-sm font-semibold leading-6 text-gray-900")
                    ux.p(account.first_name).classes("mt-1 truncate text-xs leading-5 text-gray-500")

@ui.page('/test')
def show_users():
    ui.label('Show Accounts!').classes('text-2xl m-2')


@ui.page('/show-customers-and-contracts')
def show_customers_and_contracts():
    ui.label('Übersicht Kunden und deren Verträge!').classes('text-2xl m-2')
    customers = app.db.get_list('customers', page=1, perPage=50, filter='', sort='surname,forename', cache=False)
    for customer in customers.items:
        contracts = app.db.get_list('contracts', page=1, perPage=50, filter=f'customer="{customer.id}"')
        with ux.ul().classes("divide-y divide-gray-100"):
            with ux.li().classes("flex justify-between gap-x-6 py-5"):
                with ux.div().classes("flex min-w-0 gap-x-4"):
                    with ux.div().classes("min-w-0 flex-auto"):
                        ux.p(customer.surname).classes("text-sm font-semibold leading-6 text-gray-900")
                        ux.p(customer.forename).classes("mt-1 truncate text-xs leading-5 text-gray-500")
                        ux.p('Verträge')
                        for contract in contracts.items:
                            ux.p(f'{contract.subscription}, {contract.terminal_type}')
                            # Nicegui Doc lesen, entsprechende funktionen finden
                            ui.link('Erstelle Rechnung', f'/invoice/{contract.id}')
                            ui.button('Erstelle Rechnung', on_click=lambda: ui.navigate.to(f'/invoice/{contract.id}', new_tab=True))



def default():
    with ux.div().classes('container mx-auto p-8 bg-gray-100 h-screen flex flex-col justify-center items-center'):
        with ux.div().classes('text-white p-4 mb-8 text-center'):
            ux.h1('Welcome to Vortex Company').classes('text-6xl font-extrabold tracking-wide leading-tight text-black')
            ux.div().classes('border-b-2 border-gray-300 w-full mb-8')
        # Buttons Section
        with ux.div().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'):
            button_styles = 'bg-blue-700 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full focus:outline-none focus:shadow-outline-blue'
            # Overview of Tracked Services Button
            ui.button('Overview of Tracked Services', on_click=lambda: ui.navigate.to('/show-services-trackings', new_tab=True)).classes(button_styles)
            # Userbase Button
            ui.button('Userbase', on_click=lambda: ui.navigate.to('/show-users', new_tab=True)).classes(button_styles)
            # Create Invoice Button
            ui.button('Create Invoice', on_click=lambda: ui.navigate.to('/show-customers-and-contracts', new_tab=True)).classes(button_styles)
            ux.div().classes('col-2')
            with ux.div().classes('col-3'):
                (ui.button('Subscriber Info', on_click=lambda: ui.navigate.to('/show-users'))
                .classes('text-black bg-light-green hover:bg-gray-100 py-2 px-4 border border-gray-400 rounded shadow'))
            with ux.div().classes('col-3'):
                (ui.button('Simulate Session', on_click=lambda: ui.navigate.to('/show-services-trackings'))
                 .classes('text-black bg-green hover:bg-gray-100 py-2 px-4 border border-gray-400 rounded shadow'))
            with ux.div().classes('col-3'):
                (ui.button('Send all invoices', on_click=lambda: ui.navigate.to('/show-customers-and-contracts'))
                 .classes('text-black bg-blue hover:bg-gray-100 py-2 px-4 border border-gray-400 rounded shadow'))