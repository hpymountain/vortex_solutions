from tokeo.ext.appshare import app
from winterfell.core import consts
import random

ui = app.nicegui.ui
ux = app.nicegui.ux


form_values = dict(
    contract_id='',
    terminal_type='',
    ran_type='',
    signal_quality=None,
    cur_throughput=None,
    service_type='',
    duration=0,
    sim_factor=1,
)


def service_type_select_on_change(e):
    form_values['service_type'] = e.value


@ui.refreshable
def service_type_selection():
    service_type_select_options = dict()
    if form_values['cur_throughput'] is not None:
        for service_type in consts.SERVICE_TYPES:
            if consts.SERVICE_TYPES[service_type]['min_throughput_kbytes_per_sec'] <= form_values['cur_throughput']:
                service_type_select_options[service_type] = consts.SERVICE_TYPES[service_type]['desc']
    ui.select(
        label='Service type:',
        options=service_type_select_options,
        on_change=lambda e: service_type_select_on_change(e),
    )


@ui.refreshable
def network_information():
    ran_type_desc = consts.RAN_TYPES[form_values['ran_type']]['desc'] if form_values['ran_type'] != '' else ''
    signal_quality_desc = consts.SIGNAL_QUALITIES[form_values['signal_quality']] if form_values['signal_quality'] is not None else ''
    max_throughput_desc = consts.RAN_TYPES[form_values['ran_type']]['max_throughput_desc'] if form_values['ran_type'] else ''
    cur_throughput_desc = f'{form_values["cur_throughput"]*8/1000} Mbit/s' if form_values['cur_throughput'] is not None else ''
    network_desc = f'{ran_type_desc}, Signal {signal_quality_desc}, {max_throughput_desc}, Cur {cur_throughput_desc}' if ran_type_desc != '' else ''
    ui.label(f'Network: {network_desc}')


def network_random_change():
    if form_values['contract_id'] == '':
        return
    ran_type_rnd = random.randint(0,consts.TERMINAL_TYPES[form_values['terminal_type']]['max_ran_type_idx'])
    form_values['ran_type'] = list(consts.RAN_TYPES.keys())[ran_type_rnd]
    signal_quality_rnd = random.randint(0,3)
    form_values['signal_quality'] = list(consts.SIGNAL_QUALITIES.keys())[signal_quality_rnd]
    form_values['cur_throughput'] = form_values['signal_quality'] * consts.RAN_TYPES[form_values['ran_type']]['kbyte_sec']
    network_information.refresh()
    service_type_selection.refresh()


def contract_select_on_change(e):
    form_values['contract_id'] = e.value
    form_values['terminal_type'] = app.db.get_one('contracts', form_values['contract_id']).terminal_type
    network_random_change()


def contract_selection():
    contracts = app.db.get_list('contracts', page=1, perPage=50, filter='', sort='customer.surname,customer.forename,terminal_type', q=dict(expand='customer'))
    contract_select_options = dict()
    for c in contracts.items:
        contract_select_options[c.id] = f'{c.expand["customer"].surname}, {c.expand["customer"].forename}, {consts.TERMINAL_TYPES[c.terminal_type]["desc"]}'
    ui.select(
        label='Kunde und Vertrag:',
        options=contract_select_options,
        on_change=lambda e: contract_select_on_change(e),
    )


@ui.page('/session/new')
def page_session_new():
    contract_selection()
    network_information()
    ui.button('Refresh network', on_click=lambda: network_random_change())
    service_type_selection()
    ui.button('Run', on_click=lambda: print(form_values))

# # netwrok
# ui.label
# # stats debug
# ux.div
# # session_tyoe
# select2 = ui.select({1: 'One', 2: 'Two', 3: 'Three'}).bind_value(select1, 'value')
# # minutes to simulate
# ui.number(label='Number', value=3.1415927, format='%.2f',
#           on_change=lambda e: result.set_text(f'you entered: {e.value}'))
# result = ui.label()

# # faktor
# slider = ui.slider(min=0, max=100, value=50)
# ui.label().bind_text_from(slider, 'value')

# # simulate progress
# ui.linear_progress().bind_value_from(slider, 'value')


"""
import httpx
from contextlib import contextmanager

@contextmanager
def disable(button: ui.button):
    button.disable()
    try:
        yield
    finally:
        button.enable()

async def get_slow_response(button: ui.button) -> None:
    with disable(button):
        async with httpx.AsyncClient() as client:
            response = await client.get('https://httpbin.org/delay/1', timeout=5)
            ui.notify(f'Response code: {response.status_code}')

ui.button('Get slow response', on_click=lambda e: get_slow_response(e.sender))
"""