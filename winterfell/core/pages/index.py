from tokeo.ext.appshare import app
from winterfell.core import consts

import sys
import os

os.chdir("C:\\workspace\\Software_Development_Project\\GIT\\tokeo\\winterfell")
sys.path.insert(0, 'C:\\workspace\\Software_Development_Project\\GIT\\tokeo\\winterfell')
from data_classes.user_class import read_user_from_db, read_user_list_from_db

ui = app.nicegui.ui
ux = app.nicegui.ux


@app.nicegui.fastapi_app.get('/api')
async def get_api():
    return {'msg': 'json api result'}


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
