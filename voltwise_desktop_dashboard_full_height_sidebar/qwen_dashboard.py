#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VoltWise Action Dashboard - NiceGUI Implementation
Replicates the energy management dashboard UI
"""

from nicegui import ui, app
from datetime import datetime

# Custom CSS for styling to match the original design
ui.add_css('''
    :root {
        --primary-color: #10b981;
        --primary-dark: #059669;
        --secondary-color: #3b82f6;
        --background: #f8fafc;
        --surface: #ffffff;
        --text-primary: #1e293b;
        --text-secondary: #64748b;
        --border-color: #e2e8f0;
        --success-bg: #dcfce7;
        --success-text: #166534;
        --warning-bg: #fef3c7;
        --warning-text: #92400e;
    }
    
    body {
        background: var(--background);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: var(--text-primary);
    }
    
    .dashboard-header {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
        color: white;
        padding: 1rem 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: 700;
        font-size: 1.25rem;
    }
    
    .nav-links {
        display: flex;
        gap: 0.5rem;
    }
    
    .nav-link {
        color: rgba(255,255,255,0.9);
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        transition: all 0.2s;
        display: flex;
        align-items: center;
        gap: 0.25rem;
        font-size: 0.9rem;
    }
    
    .nav-link:hover, .nav-link.active {
        background: rgba(255,255,255,0.15);
        color: white;
    }
    
    .status-banner {
        background: var(--success-bg);
        color: var(--success-text);
        padding: 0.75rem 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid var(--border-color);
        font-size: 0.9rem;
    }
    
    .price-display {
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .refresh-btn {
        background: var(--primary-color);
        color: white;
        border: none;
        padding: 0.4rem 0.8rem;
        border-radius: 0.375rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 0.25rem;
        font-size: 0.85rem;
        transition: background 0.2s;
    }
    
    .refresh-btn:hover {
        background: var(--primary-dark);
    }
    
    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .device-card {
        background: var(--surface);
        border-radius: 0.75rem;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .device-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
        font-weight: 600;
    }
    
    .device-icon {
        font-size: 1.5rem;
    }
    
    .pricing-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
    }
    
    .price-option {
        padding: 0.5rem;
        border-radius: 0.5rem;
        text-align: center;
        border: 2px solid var(--border-color);
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .price-option.start {
        border-color: var(--text-secondary);
    }
    
    .price-option.wait {
        border-color: var(--primary-color);
        background: var(--success-bg);
    }
    
    .price-option:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .price-label {
        font-size: 0.8rem;
        color: var(--text-secondary);
        margin-bottom: 0.25rem;
    }
    
    .price-value {
        font-weight: 700;
        font-size: 1.1rem;
    }
    
    .savings-badge {
        background: var(--primary-color);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem 0;
    }
    
    .wait-time {
        color: var(--text-secondary);
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }
    
    .impact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .impact-card {
        background: var(--surface);
        border-radius: 0.75rem;
        padding: 1rem;
        border: 1px solid var(--border-color);
        text-align: center;
    }
    
    .impact-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary-color);
        margin: 0.25rem 0;
    }
    
    .impact-label {
        color: var(--text-secondary);
        font-size: 0.9rem;
    }
    
    .progress-bar {
        height: 0.5rem;
        background: var(--border-color);
        border-radius: 0.25rem;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-fill {
        height: 100%;
        background: var(--primary-color);
        border-radius: 0.25rem;
        transition: width 0.3s ease;
    }
    
    .share-section {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        border-radius: 0.75rem;
        padding: 1rem;
        margin: 1.5rem 0;
        text-align: center;
    }
    
    .share-btn {
        background: white;
        color: #6366f1;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 0.5rem;
        font-weight: 600;
        margin-top: 0.5rem;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        transition: transform 0.2s;
    }
    
    .share-btn:hover {
        transform: scale(1.02);
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: var(--text-secondary);
        font-size: 0.85rem;
        border-top: 1px solid var(--border-color);
        margin-top: 2rem;
    }
    
    .rank-badge {
        background: var(--warning-bg);
        color: var(--warning-text);
        padding: 0.25rem 0.5rem;
        border-radius: 0.375rem;
        font-size: 0.8rem;
        font-weight: 600;
    }
''')

def create_navigation():
    """Create the top navigation bar"""
    with ui.element('div').classes('dashboard-header'):
        with ui.element('div').classes('logo'):
            ui.icon('bolt', size='1.5rem', color='white')
            ui.label('VoltWise')
        
        with ui.element('div').classes('nav-links'):
            for icon, label, active in [
                ('dashboard', 'Dashboard', True),
                ('history', 'Historik', False),
                ('devices', 'Enheder', False),
                ('person', 'Profil', False),
                ('settings', 'Indstillinger', False)
            ]:
                with ui.element('a').classes(f'nav-link{" active" if active else ""}'):
                    ui.icon(icon, size='1rem')
                    ui.label(label)

def create_status_banner():
    """Create the green power status banner"""
    with ui.element('div').classes('status-banner'):
        with ui.element('div'):
            ui.icon('eco', color='#166534')
            ui.label('  Status: Grøn strøm netop nu')
        with ui.element('div').style('display: flex; align-items: center; gap: 1rem;'):
            ui.label('Nuværende pris').classes('text-sm')
            ui.label('2,45 kr. pr. kWh').classes('price-display')
            with ui.button(on_click=lambda: ui.notify('Priser opdateret!')).classes('refresh-btn'):
                ui.icon('refresh', size='0.9rem')
                ui.label('Opdater pris')

def create_smart_delay_section():
    """Create the Smart Delay device cards"""
    ui.label('Smart Delay').classes('section-title')
    ui.label('Optimér dit forbrug og spar penge ved at vente.').style('color: var(--text-secondary); margin-bottom: 1rem;')
    
    devices = [
        {
            'icon': 'dishwasher',
            'name': 'Opvaskemaskine',
            'start_price': '4,50 kr.',
            'wait_price': '1,20 kr.',
            'savings': '3,30 kr.',
            'wait_time': '01:00'
        },
        {
            'icon': 'dry_cleaning',
            'name': 'Tørretumbler',
            'start_price': '6,20 kr.',
            'wait_price': '2,10 kr.',
            'savings': '4,10 kr.',
            'wait_time': '01:00'
        },
        {
            'icon': 'ev_station',
            'name': 'Elbil',
            'start_price': '45,00 kr.',
            'wait_price': '15,50 kr.',
            'savings': '29,50 kr.',
            'wait_time': '01:00'
        }
    ]
    
    for device in devices:
        with ui.element('div').classes('device-card'):
            with ui.element('div').classes('device-header'):
                ui.icon(device['icon'], classes='device-icon')
                ui.label(device['name'])
            
            with ui.element('div').classes('pricing-grid'):
                # Start now option
                with ui.element('div').classes('price-option start'):
                    ui.label('Start nu').classes('price-label')
                    ui.label(device['start_price']).classes('price-value')
                
                # Wait option
                with ui.element('div').classes('price-option wait'):
                    ui.label('Vent og spar').classes('price-label')
                    ui.label(device['wait_price']).classes('price-value')
            
            ui.label(f"Spar {device['savings']}").classes('savings-badge')
            with ui.element('div').classes('wait-time'):
                ui.icon('access_time', size='0.9rem')
                ui.label(f"Vent til kl. {device['wait_time']}")

def create_share_section():
    """Create the social sharing section"""
    with ui.element('div').classes('share-section'):
        ui.icon('emoji_events', size='1.5rem')
        ui.label('Har du en god grøn stime?').style('font-weight: 600; margin: 0.5rem 0;')
        ui.label('Del dine resultater og inspirér andre til at spare.').style('opacity: 0.9;')
        with ui.button(on_click=lambda: ui.notify('Link kopieret til udklipsholderen!')).classes('share-btn'):
            ui.icon('share')
            ui.label('Del min besparelse')

def create_impact_section():
    """Create the impact/statistics section"""
    with ui.element('div'):
        ui.label('Din Impact').classes('section-title')
        
        with ui.element('div').classes('impact-grid'):
            # Lifetime savings
            with ui.element('div').classes('impact-card'):
                ui.icon('savings', size='1.5rem', color='var(--primary-color)')
                ui.label('Livstidsbesparelse').classes('impact-label')
                ui.label('1.245,50 kr.').classes('impact-value')
                ui.label('65% af dit månedlige mål nået').style('font-size: 0.8rem; color: var(--text-secondary);')
                with ui.element('div').classes('progress-bar'):
                    with ui.element('div').classes('progress-fill').style('width: 65%'):
                        pass
            
            # CO2 reduction
            with ui.element('div').classes('impact-card'):
                ui.icon('eco', size='1.5rem', color='var(--primary-color)')
                ui.label('CO2-reduktion').classes('impact-label')
                ui.label('342 kg.').classes('impact-value')
                ui.label('Svarer til at plante 14 træer 🌲').style('font-size: 0.8rem; color: var(--text-secondary);')
            
            # Green power %
            with ui.element('div').classes('impact-card'):
                ui.icon('grid_on', size='1.5rem', color='var(--primary-color)')
                ui.label('Grøn strøm').classes('impact-label')
                ui.label('92%').classes('impact-value')
                ui.label('Månedlig rank').style('font-size: 0.8rem; color: var(--text-secondary);')
                ui.element('span').classes('rank-badge').props('icon=emoji_events').mark_slot('default', '#12 i Aarhus')
        
        # View history button
        with ui.element('div').style('text-align: center; margin-top: 1rem;'):
            with ui.button(on_click=lambda: ui.notify('Viser historik...')).props('outline'):
                ui.icon('history')
                ui.label('Se fuld historik')

def create_footer():
    """Create the page footer"""
    with ui.element('div').classes('footer'):
        ui.label('© 2024 VoltWise. Skabt med fokus på fremtidens energi.')

def build_dashboard():
    """Main function to build the complete dashboard"""
    # Page title
    ui.page_title('VoltWise Action Dashboard')
    
    # Main container
    with ui.column().style('max-width: 800px; margin: 0 auto; padding: 0 1rem;'):
        create_navigation()
        create_status_banner()
        
        with ui.element('div').style('padding: 1rem 0;'):
            create_smart_delay_section()
            create_share_section()
            create_impact_section()
        
        create_footer()

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    build_dashboard()
    ui.run(
        title='VoltWise Action Dashboard',
        favicon='⚡',
        port=8080,
        reload=True,
        dark=False
    )