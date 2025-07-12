{
    "name": "Hotel Management System",
    "author": "Agga, IdeaCode Academy",
    "license": "LGPL-3",
    "depends": ["base","web","portal","website", "contacts", "mail"],
    "data": [
        "report/booking.xml",
        "report/booking_templates.xml",

        "data/sequence.xml",

        "security/security.xml",
        "security/ir.model.access.csv",
        "views/res_partner.xml",

        "views/hms_hotel.xml",
        "views/hms_room.xml",
        "views/hms_booking.xml",

        "wizard/booking_payment_wizard.xml",

        "views/menus.xml",

        "views/hml_hotels_template.xml",
        "views/hml_room_template.xml",


    ],

    "description": """""",
    "external_dependencies": {
        "python": ["paramiko"],
    },
    "assets": {
        "web.assets_backend": [
            "technortal_hms/static/src/sample_client_action/**/*",
        ],
    },
    "demo": [
        "demo/hms_hotel.xml",
        "demo/hms_room.xml",
    ],
}
