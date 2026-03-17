#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VoltWise Design System Dashboard
Denne version demonstrerer brugen af en ekstern styling-klasse (Theme),
som radikalt reducerer støj og gør det utrolig nemt at bygge nye views fremadrettet!
"""

from nicegui import ui
from theme import Theme as T

# ============================================================================
# UI KOMPONENTER (Nu super rene takket være Theme-klassen!)
# ============================================================================

def create_sidebar():
    """Venstre sidebar navigation"""
    with ui.element('aside').classes(T.LAYOUT_SIDEBAR):
        # Logo
        with ui.element('div').classes('flex items-center gap-3 mb-12'):
            with ui.element('div').classes('bg-primary p-2 rounded-lg shadow-sm'):
                ui.label('bolt').classes(f'{T.ICON} text-[#0d1c12] block')
            ui.label('VoltWise').classes(T.H1)
        
        # Navigation
        with ui.element('nav').classes('flex-1 space-y-2'):
            nav_items = [
                {'icon': 'dashboard', 'label': 'Dashboard', 'active': True},
                {'icon': 'history', 'label': 'Historik', 'active': False},
                {'icon': 'devices', 'label': 'Enheder', 'active': False},
                {'icon': 'person', 'label': 'Profil', 'active': False},
            ]
            
            for item in nav_items:
                state_class = T.NAV_ACTIVE if item['active'] else T.NAV_INACTIVE
                with ui.link(target='#').classes(f'{T.NAV_BASE} {state_class}'):
                    ui.label(item['icon']).classes(T.ICON)
                    ui.label(item['label'])
                
        # Indstillinger (bund)
        with ui.element('div').classes('pt-8 border-t border-nordic-gray mt-auto'):
            with ui.link(target='#').classes(f'{T.NAV_BASE} {T.NAV_INACTIVE}'):
                ui.label('settings').classes(T.ICON)
                ui.label('Indstillinger')

def create_top_header():
    """Top bar med notifikationer og profilbillede"""
    with ui.element('header').classes('flex items-center justify-between mb-12 w-full'):
        ui.element('div') # Tom space (Spacer)
        
        with ui.element('div').classes('flex items-center gap-4'):
            with ui.button(color=None).props('unelevated no-caps').classes(T.BTN_ICON):
                ui.label('notifications').classes(f'{T.ICON} {T.TEXT_MUTED}')
            
            # Profil avatar
            avatar_url = 'https://lh3.googleusercontent.com/aida-public/AB6AXuCzYwTRHD7eBsRfu-BhXlfSEeOvNq0yeUEPwwhbowu1VHthaRqxOtG9tMgOnragTGNp0OtUGESb4POKChOsOT_FQkmmUNynqjGPPlrPY5vcqQbABA3H1G8AG2eQPaySxEGAUIh6c7pgAdLgAzpzn9bflXHK_yHLnvRXhEjr1R-7Wk3DH7Q_klqbYIAX9SEsvNXrQFl_eWacMHVSoRK3Xxj-jvBmofvDNLbGyQMiGH0fymIKg5p4OHFR2pf9Yx9dEdvygxzy704Q6Xo'
            ui.element('div').classes(T.AVATAR).style(f"background-image: url('{avatar_url}')")

def create_hero_section():
    """Helte-sektionen med aktuel pris"""
    with ui.element('section').classes(T.HERO_BANNER):
        # Status indikator
        with ui.element('div').classes(T.BADGE_LITE):
            ui.element('span').classes('w-2 h-2 rounded-full bg-primary animate-pulse')
            ui.label('Status: Grøn strøm netop nu')
        
        # Pris display
        with ui.element('div').classes('flex flex-col items-center mt-4'):
            ui.label('Nuværende pris').classes(f'{T.TEXT_MUTED} font-medium mb-1')
            with ui.element('h2').classes(T.H2):
                ui.label('2,45').classes('inline')
                ui.label('kr. pr. kWh').classes('text-3xl opacity-60 ml-2 inline')
                
        # Opdater knap
        with ui.button(color=None).props('unelevated no-caps').classes(f'{T.BTN_DARK} mt-10'):
            ui.label('refresh').classes(T.ICON)
            ui.label('Opdater pris')

def create_smart_delay_section():
    """Visning af enheder og mulige besparelser"""
    with ui.element('section'):
        # Header
        with ui.element('div').classes('flex items-center justify-between mb-8'):
            with ui.element('div'):
                ui.label('Smart Delay').classes(T.H3)
                ui.label('Optimér dit forbrug og spar penge ved at vente.').classes(T.TEXT_MUTED)
            with ui.element('div').classes(T.LINK_PRIMARY):
                ui.label('Se alle enheder')
                ui.label('arrow_forward').classes(f'{T.ICON} text-sm')
                
        # Enheder
        devices = [
            {'icon': 'dishwasher', 'name': 'Opvaskemaskine', 'now': '4,50 kr.', 'later': '1,20 kr.', 'save': '3,30 kr.'},
            {'icon': 'dry_cleaning', 'name': 'Tørretumbler', 'now': '6,20 kr.', 'later': '2,10 kr.', 'save': '4,10 kr.'},
            {'icon': 'ev_station', 'name': 'Elbil', 'now': '45,00 kr.', 'later': '15,50 kr.', 'save': '29,50 kr.'}
        ]
        
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-3 gap-6'):
            for dev in devices:
                with ui.element('div').classes(T.CARD):
                    with ui.element('div').classes(T.ICON_BOX):
                        ui.label(dev['icon']).classes(T.ICON)
                    
                    ui.label(dev['name']).classes(T.H4)
                    
                    with ui.element('div').classes('space-y-3 mb-8'):
                        with ui.element('div').classes('flex justify-between text-sm'):
                            ui.label('Start nu').classes(T.TEXT_MUTED)
                            ui.label(dev['now']).classes('font-semibold')
                        with ui.element('div').classes('flex justify-between text-sm'):
                            ui.label('Vent og spar').classes(T.TEXT_MUTED)
                            ui.label(dev['later']).classes('font-semibold text-primary-dark')
                            
                    with ui.element('div').classes('mt-auto space-y-3'):
                        ui.label(f"Spar {dev['save']}").classes(T.BADGE_FILLED)
                        ui.label('Vent til kl. 01:00').classes(T.BTN_BLOCK_DARK)

def create_social_section():
    """Dele-funktion"""
    with ui.element('section').classes(T.WIDGET_PANEL):
        with ui.element('div').classes('flex items-center gap-6'):
            with ui.element('div').classes(T.ICON_CIRCLE):
                ui.label('emoji_events').classes(T.ICON)
            with ui.element('div'):
                ui.label('Har du en god grøn stime?').classes('text-xl font-bold')
                ui.label('Del dine resultater og inspirér andre til at spare.').classes(T.TEXT_MUTED)
        
        with ui.button(color=None).props('unelevated no-caps').classes(T.BTN_PRIMARY):
            ui.label('share').classes(T.ICON)
            ui.label('Del min besparelse')

def create_impact_sidebar():
    """Højre sidebar med brugerens 'Impact' statestik"""
    with ui.element('aside').classes('lg:col-span-3 space-y-8 h-full flex-shrink-0'):
        with ui.element('div').classes(T.SIDEBOX):
            
            with ui.element('h3').classes('text-xl font-bold mb-8 flex items-center gap-2'):
                ui.label('monitoring').classes(f'{T.ICON} text-primary-dark')
                ui.label('Din Impact')
            
            # Penge sparet
            with ui.element('div').classes('mb-10'):
                with ui.element('div').classes('flex items-center gap-2 mb-2'):
                    ui.label('savings').classes(f'{T.ICON} {T.TEXT_MUTED_SM}')
                    ui.label('Livstidsbesparelse').classes(T.TEXT_MUTED_SM)
                
                with ui.element('div').classes('text-3xl font-black text-[#0d1c12]'):
                    ui.label('1.245,50 ').classes('inline')
                    ui.label('kr.').classes('text-lg font-bold opacity-60 inline')
                
                with ui.element('div').classes(T.PROGRESS_BG):
                    ui.element('div').classes(T.PROGRESS_FILL).style('width: 65%')
                ui.label('65% af dit månedlige mål nået').classes('text-xs text-gray-500 mt-2 font-medium')

            # CO2 Reduktion
            with ui.element('div').classes('mb-10'):
                with ui.element('div').classes('flex items-center gap-2 mb-2'):
                    ui.label('eco').classes(f'{T.ICON} {T.TEXT_MUTED_SM}')
                    ui.label('CO2-reduktion').classes(T.TEXT_MUTED_SM)
                
                with ui.element('div').classes('text-3xl font-black text-[#0d1c12]'):
                    ui.label('342 ').classes('inline')
                    ui.label('kg.').classes('text-lg font-bold opacity-60 inline')
                
                with ui.element('p').classes('text-xs text-gray-500 mt-2 font-medium'):
                    ui.label('Svarer til at plante ').classes('inline')
                    ui.label('14 træer').classes('text-primary-dark font-bold inline')
                    ui.label(' 🌲').classes('inline')

            # Flere Stats
            with ui.element('div').classes('space-y-4 pt-8 border-t border-nordic-gray'):
                with ui.element('div').classes('flex items-center justify-between text-sm'):
                    ui.label('Grøn strøm %').classes(T.TEXT_MUTED)
                    ui.label('92%').classes('font-bold text-primary-dark')
                with ui.element('div').classes('flex items-center justify-between text-sm'):
                    ui.label('Månedlig rank').classes(T.TEXT_MUTED)
                    ui.label('#12 i Aarhus').classes(T.TEXT_STRONG)
            
            # CTA
            ui.label('Se fuld historik').classes(T.BTN_BLOCK_LIGHT)

# ============================================================================
# HOVEDSIDE
# ============================================================================

@ui.page('/')
def dashboard():
    T.setup()

    # Root layout flexbox container
    with ui.element('div').classes(T.LAYOUT_ROOT):
        create_sidebar()
        
        # Main Content Area
        with ui.element('div').classes(T.LAYOUT_MAIN):
            create_top_header()
            
            # Grid til opdeling
            with ui.element('div').classes(T.LAYOUT_GRID):
                
                # Center indholds-kolonne
                with ui.element('main').classes('lg:col-span-9 space-y-16'):
                    create_hero_section()
                    create_smart_delay_section()
                    create_social_section()
                
                # Højre kolonne
                create_impact_sidebar()
            
            # Footer
            with ui.element('footer').classes('mt-20 pt-12 border-t border-nordic-gray text-center text-gray-400 text-sm pb-12'):
                ui.label('© 2024 VoltWise. Skabt med fokus på fremtidens energi.')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='VoltWise Design System Dashboard')
