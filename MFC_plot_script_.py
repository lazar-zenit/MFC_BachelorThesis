import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("data_file.xls")

print(data)

#respirometry
#H2 Accum
"""
plt.xlabel("Vreme [sat]")
plt.ylabel("$H_2$ Akumulacija (mL)")
plt.plot(data["Time 1"], data["H2 Accum 1"], label="Kontrola")
#plt.plot(data["Time 2"], data["H2 Accum 2"], label="Kontrola")
#.plot(data["Time 3"], data["H2 Accum 3"], label="Uzorak 1a 10 g")
#plt.plot(data["Time 4"], data["H2 Accum 4"], label="Uzorak 1b 10 g")
plt.plot(data["Time 5"], data["H2 Accum 5"], label="Uzorak sedimenta sa SRB bakterijama")
#plt.plot(data["Time 6"], data["H2 Accum 6"], label="Uzorak 2b 20 g")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Akumulacija vodonika ($H_2$)")
plt.axhline(0, c='black', ls='--')
plt.savefig('H2.png',bbox_inches='tight', dpi=300,)
plt.xlim(left=0)
"""
#CO Accum
"""
plt.xlabel("Vreme [sat]")
plt.ylabel("$CO$ Akumulacija (mL)")
#plt.plot(data["Time 1"], data["CO Accum 1"], label="Kontrola 10 g")
plt.plot(data["Time 2"], data["CO Accum 2"], label="Kontrola")
#plt.plot(data["Time 3"], data["CO Accum 3"], label="Uzorak 1a 10 g")
#plt.plot(data["Time 4"], data["CO Accum 4"], label="Uzorak 1b 10 g")
#plt.plot(data["Time 5"], data["CO Accum 5"], label="Uzorak 2a 20 g")
plt.plot(data["Time 6"], data["CO Accum 6"], label="Uzorak sedimenta sa SRB bakterijama")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Akumulacija metana ($CO$)")
plt.axhline(0, c='black', ls='--')
plt.savefig('CO.png',bbox_inches='tight', dpi=300,)
"""
#CH4 Accum
"""
plt.xlabel("Vreme [sat]")
plt.ylabel("$CH_4$ Akumulacija (mL)")
#plt.plot(data["Time 1"], data["CH4 Accum 1"], label="Kontrola 10 g")
plt.plot(data["Time 2"], data["CH4 Accum 2"], label="Kontrola")
#plt.plot(data["Time 3"], data["CH4 Accum 3"], label="Uzorak 1a 10 g")
#plt.plot(data["Time 4"], data["CH4 Accum 4"], label="Uzorak 1b 10 g")
#plt.plot(data["Time 5"], data["CH4 Accum 5"], label="Uzorak 2a 20 g")
plt.plot(data["Time 6"], data["CH4 Accum 6"], label="Uzorak sedimenta sa SRB bakterijama")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Akumulacija metana ($CH_4$)")
plt.axhline(0, c='black', ls='--')
plt.savefig('CH4.png',bbox_inches='tight', dpi=300,)
"""
#O2 accumulation

"""
plt.xlabel("Vreme [sat]")
plt.ylabel("$O_2$ Akumulacija (mL)")
plt.plot(data["Time 1"], data["O2 Accum 1"], label="Kontrola")
#plt.plot(data["Time 2"], data["O2 Accum 2"], label="Kontrola 20 g")
#plt.plot(data["Time 3"], data["O2 Accum 3"], label="Uzorak 1a 10 g")
#plt.plot(data["Time 4"], data["O2 Accum 4"], label="Uzorak 1b 10 g")
plt.plot(data["Time 5"], data["O2 Accum 5"], label="Uzorak sedimenta sa SRB bakterijama")
#plt.plot(data["Time 6"], data["O2 Accum 6"], label="Uzorak 2b 20 g")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Akumulacija kiseonika ($O_2$)")
plt.ylim(top=0)
plt.xlim(left=0)
plt.savefig('O2.png',bbox_inches='tight', dpi=300,)
"""
#CO2 
"""
plt.xlabel("Vreme [sat]")
plt.ylabel("$CO_2$ Akumulacija (mL)")
plt.plot(data["Time 1"], data["CO2 Accum 1"], label="Kontrola")
#plt.plot(data["Time 2"], data["CO2 Accum 2"], label="Kontrola 20 g")
#plt.plot(data["Time 3"], data["CO2 Accum 3"], label="Uzorak 1a 10 g")
#plt.plot(data["Time 4"], data["CO2 Accum 4"], label="Uzorak 1b 10 g")
plt.plot(data["Time 5"], data["CO2 Accum 5"], label="Uzorak sedimenta sa SRB bakterijama")
#plt.plot(data["Time 6"], data["CO2 Accum 6"], label="Uzorak 2b 20 g")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Akumulacija kiseonika ($CO_2$)")
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.savefig('CO2.png',bbox_inches='tight', dpi=300,)
"""


#bar plot for number of microorganisms
"""
podloge=['BA', 'HA', 'SRA', 'PSA']
CFU=[5.20E+06, 1.73E+07, 1.63E+06, 2.00E+02]
plt.ylabel('Broj mikroorganizama (CFU/g)')
plt.bar(podloge, CFU)
plt.ylim(top=2.0E+07)
plt.savefig('Br_MO.png',bbox_inches='tight', dpi=300,)
"""

#x=dani, y=mWm2
"""
plt.xlabel("Vreme [dan]")
plt.ylabel("Gustina snage [$mW/m^2$]")
plt.plot(data["D"], data["R1"], label="1 kΩ", marker=".")
plt.plot(data["D"], data["R2"], label="2,2 kΩ",  marker="p")
plt.plot(data["D"], data["R3"], label="4,7 kΩ",  marker="o")
plt.plot(data["D"], data["R4"], label="10"" kΩ",  marker="v")
plt.plot(data["D"], data["R5"], label="22 kΩ", marker="^")
plt.plot(data["D"], data["R6"], label="56 kΩ", marker="<")
plt.plot(data["D"], data["R7"], label="100 kΩ", marker=">")
plt.plot(data["D"], data["R8"], label="220 kΩ", marker="1")
plt.plot(data["D"], data["R9"], label="470 kΩ",  marker="8")
plt.plot(data["D"], data["R10"], label="1 kΩ",  marker="s")
plt.plot(data["D"], data["R11"], label="2,2 MΩ",  marker="P")
plt.plot(data["D"], data["R12"], label="4,7 MΩ",  marker="H")
plt.plot(data["D"], data["R13"], label="10 MΩ",  marker="X")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Ćelija 3")
plt.savefig('C3_mWm2_vs_dani.png',bbox_inches='tight', dpi=300,)
"""

#x=mAm2, y=mV
"""
plt.xlabel("Gustina struje [$mA/m^2$]")
plt.ylabel("Napon pod otporom [mV]")
plt.plot(data["A1"], data["U1"], label="Dan 1", marker=".")
plt.plot(data["A2"], data["U2"], label="Dan 2",  marker="p")
plt.plot(data["A3"], data["U3"], label="Dan 3",  marker="o")
plt.plot(data["A4"], data["U4"], label="Dan 4",  marker="v")
plt.plot(data["A7"], data["U7"], label="Dan 7", marker="^")
plt.plot(data["A9"], data["U9"], label="Dan 9", marker="<")
plt.plot(data["A10"], data["U10"], label="Dan 10", marker=">")
plt.plot(data["A11"], data["U11"], label="Dan 11", marker="1")
plt.plot(data["A14"], data["U14"], label="Dan 14",  marker="8")
plt.plot(data["A15"], data["U15"], label="Dan 15",  marker="s")
plt.ylim(top=350)
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Ćelija 3")
plt.savefig('C3_mV_vs_mAm_tret.png',bbox_inches='tight', dpi=300,)
"""

#x=kOhm, y=mWm2, mAm2
"""
plt.xlabel("Otpor [kΩ]")
plt.ylabel("Gustina snage [$mW/m^2$]")
plt.semilogx(data["R"], data["D1"], label="Dan 1", marker=".")
plt.semilogx(data["R"], data["D2"], label="Dan 2",  marker="p")
plt.semilogx(data["R"], data["D3"], label="Dan 3",  marker="o")
plt.semilogx(data["R"], data["D4"], label="Dan 4",  marker="v")
plt.semilogx(data["R"], data["D7"], label="Dan 7", marker="^")
plt.semilogx(data["R"], data["D9"], label="Dan 9", marker="<")
plt.semilogx(data["R"], data["D10"], label="Dan 10", marker=">")
plt.semilogx(data["R"], data["D11"], label="Dan 11", marker="1")
plt.semilogx(data["R"], data["D14"], label="Dan 14", marker="2")
plt.semilogx(data["R"], data["D15"], label="Dan 15", marker="3")
plt.ylim(top=6)
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Ćelija 3")
plt.savefig('C3_mWm2_vs_kOhm_tret.png',bbox_inches='tight', dpi=300,)
"""

#x=ohm, y=mV
"""
plt.xlabel("Otpor [kΩ]")
plt.ylabel("Napon pod otporom [mV]")
plt.semilogx(data["R"], data["D1"], label="Dan 1", marker=".")
plt.semilogx(data["R"], data["D2"], label="Dan 2",  marker="p")
plt.semilogx(data["R"], data["D3"], label="Dan 3",  marker="o")
plt.semilogx(data["R"], data["D4"], label="Dan 4",  marker="v")
plt.semilogx(data["R"], data["D7"], label="Dan 7", marker="^")
plt.semilogx(data["R"], data["D9"], label="Dan 9", marker="<")
plt.semilogx(data["R"], data["D10"], label="Dan 10", marker=">")
plt.semilogx(data["R"], data["D11"], label="Dan 11", marker="1")
plt.semilogx(data["R"], data["D14"], label="Dan 14",  marker="8")
plt.semilogx(data["R"], data["D15"], label="Dan 15",  marker="s")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Ćelija 3")
plt.savefig('C3_mV_vs_kOhm_tret.png',bbox_inches='tight', dpi=300,)
"""

#OCV thorugh days
"""
plt.xlabel("Vreme [dan]")
plt.ylabel("Napon otvorenog kola [mV]")
plt.plot(data["D"], data["K"], label="Kontrola")
plt.plot(data["D"], data["c1"], label="Ćelija 1")
plt.plot(data["D"], data["c2"], label="Ćelija 2")
plt.plot(data["D"], data["c3"], label="Ćelija 3")
plt.legend()                        
plt.savefig('OCV_po_danima_tret.png',bbox_inches='tight', dpi=300,)
"""

#double x-axis, polarisation curves
"""
fig,ax = plt.subplots()
ax.set_xlabel("Gustina struje [$mA/m^2$]")
ax.set_ylabel("Napon pod otporom [mV]")
ax.plot(data["I"], data["U"],marker="^", color="r", label="Napon pod otporom")
#ax.set_ylim(top=350, bottom=25)
ax2=ax.twinx()
ax2.plot(data["I"], data["P"],marker="<",color="b", label="Gustina snage")
ax2.set_ylabel("Gustina snage[$mW/m^2$]")
#ax2.set_ylim(top=10, bottom=0)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.title("Ćelija 3")
plt.savefig('C3_pol_kriva_dan9.png',bbox_inches='tight', dpi=300,)
