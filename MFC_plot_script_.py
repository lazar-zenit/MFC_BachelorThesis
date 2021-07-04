import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel("working_data_file.xls")

print(data)

#x=kOhm, y=mWm2, mAm2

plt.xlabel("Otpor [kΩ]")
plt.ylabel("Gustina struje [$mA/m^2$]")
plt.semilogx(data["R"], data["D1"], label="Dan 1", marker=".")
plt.semilogx(data["R"], data["D2"], label="Dan 2",  marker="p")
plt.semilogx(data["R"], data["D3"], label="Dan 3",  marker="o")
plt.semilogx(data["R"], data["D4"], label="Dan 4",  marker="v")
plt.semilogx(data["R"], data["D7"], label="Dan 7", marker="^")
plt.semilogx(data["R"], data["D8"], label="Dan 8", marker="<")
plt.semilogx(data["R"], data["D9"], label="Dan 9*", marker=">")
plt.semilogx(data["R"], data["D10"], label="Dan 10*", marker="1")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Ćelija 3")
plt.savefig('C3_mAm2_vs_kOhm.png',bbox_inches='tight', dpi=300,)


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
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Kontrola")
plt.savefig('C_mWm2_vs_dani_tret.png',bbox_inches='tight', dpi=300,)
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
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Ćelija 3")
plt.savefig('C3_mV_vs_mAm2_tret.png',bbox_inches='tight', dpi=300,)
"""

#x=ohm, y=mV
"""
plt.xlabel("Otpor [kΩ]")
plt.ylabel("Napon pod otporom [mV]")
plt.semilogx(data["R"], data["d1"], label="Dan 1", marker=".")
plt.semilogx(data["R"], data["d2"], label="Dan 2",  marker="p")
plt.semilogx(data["R"], data["d3"], label="Dan 3",  marker="o")
plt.semilogx(data["R"], data["d4"], label="Dan 4",  marker="v")
plt.semilogx(data["R"], data["d7"], label="Dan 7", marker="^")
plt.semilogx(data["R"], data["d9"], label="Dan 9", marker="<")
plt.semilogx(data["R"], data["d10"], label="Dan 10", marker=">")
plt.semilogx(data["R"], data["d11"], label="Dan 11", marker="1")
plt.semilogx(data["R"], data["d14"], label="Dan 14",  marker="8")
plt.semilogx(data["R"], data["d15"], label="Dan 15",  marker="s")
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, title="Ćelija 3")
plt.savefig('C3_mV_vs_kOhm_tret.png',bbox_inches='tight', dpi=300,)
"""

#OCV throughout days
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

#double x-axis
"""
fig,ax = plt.subplots()
ax.set_xlabel("Gustina struje [$mA/m^2$]")
ax.set_ylabel("Napon pod otporom [mV]")
ax.plot(data["I"], data["U"],marker="^", color="r", label="Napon pod otporom")
ax2=ax.twinx()
ax2.plot(data["I"], data["P"],marker="<",color="b", label="Gustina snage")
ax2.set_ylabel("Gustina snage[$mW/m^2$]")
ax2.legend(loc=0)
ax.legend(loc=0)
plt.title("Ćelija 3")
plt.savefig('C3_pol_kriva_dan9.png',bbox_inches='tight', dpi=300,)
"""