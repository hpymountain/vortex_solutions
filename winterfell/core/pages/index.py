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
            ui.button('Add Contract', on_click=lambda: ui.notify("This function is not implemented yet :("))
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

    ui.button('OK', on_click = edit_user)

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
    ux.h1('This is the homepage!').classes('text-2xl m-2')
    ui.link('Übersicht der User', '/show-users')
    ui.link('Übersicht Tracked Services', '/show-services-trackings')
    ui.link('Übersicht Justus', '/show-justus')
    ui.link('Erstelle Rechnungen', '/show-customers-and-contracts')

