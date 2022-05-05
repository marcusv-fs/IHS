cmd_/home/marcus/IHS/Module.symvers := sed 's/\.ko$$/\.o/' /home/marcus/IHS/modules.order | scripts/mod/modpost -m -a  -o /home/marcus/IHS/Module.symvers -e -i Module.symvers   -T -
