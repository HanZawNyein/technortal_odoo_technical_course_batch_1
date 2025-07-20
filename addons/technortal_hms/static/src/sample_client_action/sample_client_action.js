import {registry} from "@web/core/registry";

import {Component, useRef,useState,onWillStart} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";

class SampleClientAction extends Component {
    static template = "technortal_hms.SampleClientAction";

    setup() {
        this.searchRef = useRef('search-input');
        this.state = useState({
            partners: [
                // {id: 1, name: 'A'},
                // {id: 2, name: 'B'},
            ]
        })
        this.ormService = useService('orm');
        onWillStart(async ()=>{
            await this.getAllPartners()
        })
    }

    async getAllPartners() {
        this.state.partners = await this.ormService.searchRead('res.partner', [], ['id', 'display_name'])
    }

    async search() {
        // console.log("hrllo")
        // console.log()
        let data = this.searchRef.el.value;
        if(data){
            this.state.partners = this.state.partners.filter(partner=>partner.display_name === data)
        }else {
            await  this.getAllPartners();
        }
        this.searchRef.el.value = null;
    }
}

// remember the tag name we put in the first step
registry.category("actions").add("technortal_hms.SampleClientAction", SampleClientAction);