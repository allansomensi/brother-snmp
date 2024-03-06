from pysnmp import hlapi as snmp


class Printer:
    def __init__(self, name, model, ip_address, is_colored, has_drum, oid_map):
        self.name = name
        self.model = model
        self.ip_address = ip_address
        self.is_colored = is_colored
        self.has_drum = has_drum
        self.oid_map = oid_map

    def get_oid(self, oid_name):
        oid_value = self.oid_map.get(oid_name)

        if not oid_value:
            raise ValueError(f"Invalid OID name: {oid_name}")

        error_indication, error_status, error_index, var_binds = next(
            snmp.getCmd(
                snmp.SnmpEngine(),
                snmp.CommunityData("public"),
                snmp.UdpTransportTarget((self.ip_address, 161)),
                snmp.ContextData(),
                snmp.ObjectType(snmp.ObjectIdentity(oid_value)),
            )
        )

        if error_indication:
            print(f"Error: {error_indication}")
        elif error_status:
            print(f"SNMP Error: {error_status}")
        else:
            return var_binds[0][1].prettyPrint()

    def get_mac(self):
        mac_hex = self.get_oid("oid_mac")
        mac_formatted = ":".join(
            [mac_hex[i : i + 2] for i in range(2, len(mac_hex), 2)]
        ).upper()
        return mac_formatted

    def get_vendor(self):
        return self.get_oid("oid_vendor")

    def get_language(self):
        return self.get_oid("oid_language")

    def get_uptime(self):
        timeticks = int(self.get_oid("oid_uptime"))
        total_seconds = timeticks // 100

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return f"{hours} h, {minutes} min e {seconds} seg"

    def get_status(self):
        return self.get_oid("oid_status")

    def get_toner(self, color):
        maintenance_hex = self.get_oid("oid_info_maintenance")
        start = None

        if color == "black":
            start = maintenance_hex.find("6f")
        elif color == "cyan":
            start = maintenance_hex.find("70")
        elif color == "magenta":
            start = maintenance_hex.find("71")
        elif color == "yellow":
            start = maintenance_hex.find("72")

        hex = maintenance_hex[start + 2 : start + 14]
        toner_level = int(hex[4:], 16)

        return f"{toner_level // 100}%"

    def get_drum(self):
        maintenance_hex = self.get_oid("oid_info_maintenance")
        start = maintenance_hex.find("41")
        substring = maintenance_hex[start + 2 : start + 14]
        drum_level = int(substring[4:], 16)

        return f"{drum_level // 100}%"

    def get_toner_models(self):
        return self.get_oid("oid_mac")

    def get_total_pages(self):
        return self.get_oid("oid_count_pages")

    def get_count_pages_double_sided(self):
        return self.get_oid("oid_count_pages_double_sided")

    def get_total_copies(self):
        return self.get_oid("oid_count_copies")

    def get_count_copies_double_sided(self):
        return self.get_oid("oid_count_copies_double_sided")

    def get_total_pages_pc(self):
        return self.get_oid("oid_count_pages_pc")

    def get_count_pages_pc_double_sided(self):
        return self.get_oid("oid_count_pages_pc_double_sided")

    def get_total_pages_a4_letter(self):
        return self.get_oid("oid_count_pages_a4_letter")

    def get_total_pages_legal_a4_long(self):
        return self.get_oid("oid_count_pages_legal_a4_long")

    def get_total_pages_b5_executive(self):
        return self.get_oid("oid_count_pages_b5_executive")

    def get_total_pages_envelope(self):
        return self.get_oid("oid_count_pages_envelope")

    def get_total_pages_a5(self):
        return self.get_oid("oid_count_pages_a5")

    def get_total_pages_other(self):
        return self.get_oid("oid_count_pages_other")
