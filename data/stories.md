## Network Happy Path + Role Happy Path
* greet
  - utter_intro
* rights_inquiry
  - utter_check_network
* affirm
  - utter_check_role  
* affirm
  - utter_create_ticket
* affirm
  - helpdesk_form
  - form{"name": "helpdesk_form"}
  - form{"name": null}
* affirm
  - utter_anything_else
* deny
  - utter_goodbye

## Network Happy Path + Role Sad Path + Ticket Creation
* greet
  - utter_intro
* rights_inquiry
  - utter_check_network
* affirm
  - utter_check_role  
* deny
  - utter_contact_coo
  - utter_or
  - utter_create_ticket
* affirm
  - helpdesk_form
  - form{"name": "helpdesk_form"}
  - form{"name": null}
* affirm
  - utter_anything_else
* deny
  - utter_goodbye
  
## Network Happy Path + Role Sad Path + No Ticket Creation
* greet
  - utter_intro
* rights_inquiry
  - utter_check_network
* affirm
  - utter_check_role  
* deny
  - utter_contact_coo
  - utter_or
  - utter_create_ticket
* deny
  - utter_anything_else
* deny
  - utter_goodbye

## Network Sad Path
* greet
  - utter_intro
* rights_inquiry
  - utter_check_network
* deny
  - utter_portal_access
   
 ## Network Issue
* greet
  - utter_intro
* network_issue
  - utter_check_network
* affirm
  - utter_check_role
* affirm
  - utter_create_ticket
* affirm
  - helpdesk_form
  - form{"name": "helpdesk_form"}
  - form{"name": null}
* affirm
  - utter_anything_else
* deny
  - utter_goodbye
  
## Name Happy Path
* name_entry
  - utter_name_intro
* rights_inquiry
  - utter_check_network
* affirm
  - utter_check_role  
* affirm
  - utter_create_ticket
* affirm
  - helpdesk_form
  - form{"name": "helpdesk_form"}
  - form{"name": null}
* affirm
  - utter_anything_else
* deny
  - utter_goodbye
  
## OTP Sad Path + Other Request
* greet
  - utter_intro
* otp_request
  - utter_otp_check
* thanks
  - utter_anything_else_global
* affirm
  - utter_happy
  
## OTP Sad Path + No Other Request
* greet
  - utter_intro
* otp_request
  - utter_otp_check
* thanks
  - utter_anything_else_global
* deny
  - utter_goodbye