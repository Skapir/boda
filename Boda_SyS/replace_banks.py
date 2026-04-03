import os
import re

filepath = r'c:\Users\SKAPIR\Desktop\Boda_SyS\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the bank accounts before the "Ver Sugerencias" button
bank_html = """
                <div style="text-align: left; background: #f9f9f9; padding: 15px; border-radius: 10px; margin-bottom: 12px; border-left: 4px solid #002A8D; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <h4 style="color: #002A8D; margin-bottom: 5px; font-size:1.1rem;"><i class="fas fa-university"></i> BBVA</h4>
                    <p style="margin: 3px 0; font-size: 0.95rem;"><strong>Cuenta:</strong> 0011-0842-0200030948</p>
                    <p style="margin: 3px 0; font-size: 0.95rem;"><strong>CCI:</strong> 01184200020003094820</p>
                </div>
                <div style="text-align: left; background: #f9f9f9; padding: 15px; border-radius: 10px; margin-bottom: 12px; border-left: 4px solid #FF7800; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <h4 style="color: #FF7800; margin-bottom: 5px; font-size:1.1rem;"><i class="fas fa-university"></i> BCP</h4>
                    <p style="margin: 3px 0; font-size: 0.95rem;"><strong>Cuenta:</strong> 19198693270069</p>
                    <p style="margin: 3px 0; font-size: 0.95rem;"><strong>CCI:</strong> 00219119869327006952</p>
                </div>
                <div style="text-align: left; background: #f9f9f9; padding: 15px; border-radius: 10px; margin-bottom: 12px; border-left: 4px solid #00A453; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <h4 style="color: #00A453; margin-bottom: 5px; font-size:1.1rem;"><i class="fas fa-university"></i> Interbank</h4>
                    <p style="margin: 3px 0; font-size: 0.95rem;"><strong>Cuenta:</strong> 898 3300672851</p>
                    <p style="margin: 3px 0; font-size: 0.95rem;"><strong>CCI:</strong> 00389801330067285142</p>
                </div>
                <div style="display: flex; justify-content: space-between; gap: 10px; margin-bottom: 25px;">
                    <div style="text-align: center; border: 1px solid #eee; padding: 10px; border-radius: 10px; background: #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.03); flex: 1;">
                        <h4 style="color: #74205C; margin-bottom: 5px; font-size: 1rem;"><i class="fas fa-mobile-alt"></i> Yape</h4>
                        <p style="font-weight: 800; font-size: 1rem; color: #333;">994 400 662</p>
                    </div>
                    <div style="text-align: center; border: 1px solid #eee; padding: 10px; border-radius: 10px; background: #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.03); flex: 1;">
                        <h4 style="color: #08af29e6; margin-bottom: 5px; font-size: 1rem;"><i class="fas fa-mobile-alt"></i> Plin</h4>
                        <p style="font-weight: 800; font-size: 1rem; color: #333;">994 400 662</p>
                    </div>
                </div>
                <p style="margin-bottom: 25px; font-size: 0.95rem; color: #555; text-align: center;">Cuentas a nombre de: <br><strong style="font-size: 1.2rem; color: var(--color-green);">Sergio Kevin Perez Nateros</strong></p>

                <button class="btn-submit" onclick="document.getElementById('regalos-modal').style.display='flex'"
"""

target_btn = """                <button class="btn-submit" onclick="document.getElementById('regalos-modal').style.display='flex'\""""
html = html.replace(target_btn, bank_html)

# Remove the entire div #bancosModal
html = re.sub(r'<!-- MODAL BANCOS -->(.*?)<!-- MODAL MAPA GOOGLE -->', '<!-- MODAL MAPA GOOGLE -->', html, flags=re.DOTALL)

# Remove onclick from gifts
html = html.replace("""onclick="document.getElementById('regalos-modal').style.display='none'; document.getElementById('bancosModal').style.display='flex'\"""", "")
html = html.replace("""cursor: pointer;""", "")

# Update the exact "Hacer un aporte" button text to close the modal
html = re.sub(r'<button class="btn-regalar"\s*(.*?)>Hacer[\r\n\s]*un aporte</button>', r'<button class="btn-regalar" onclick="document.getElementById(\'regalos-modal\').style.display=\'none\'" \1>Cerrar Sugerencias</button>', html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Hecho")
