import { registry } from "@web/core/registry";

import { Component } from  "@odoo/owl";

class SampleClientAction extends Component {
    static template = "technortal_hms.SampleClientAction";
}

// remember the tag name we put in the first step
registry.category("actions").add("technortal_hms.SampleClientAction", SampleClientAction);