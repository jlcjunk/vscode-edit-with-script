#!/usr/bin/env python3

#   simply output a template - Terraform CR in this case


template = """
#███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#   CR_
#   
#   story_id
#   
#   
#   
#   
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#   create and plan terraform code
#---------------------------------------------------------------------------------------------------
##  be sure starting from most recent commit to master - loses all changes

cd ~/src2/bitbucket/terraform/edge/


git checkout -f master 
git status -s | egrep .
git status -s | egrep '^\?' | sed 's~^...~~g' | xargs -I '{}' rm -rf '{}'
git pull --recurse-submodules



##    clean up auto generated terraform files & correct formatting - list all stacks to be worked on

for d in $( echo "$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_a
$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_b
$HOME/src2/bitbucket/terraform/edge/stacks/a104_11_edge_fortigate_configure_a
$HOME/src2/bitbucket/terraform/edge/stacks/a104_11_edge_fortigate_configure_b
$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_pci_fortigate_configure_a
$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_pci_fortigate_configure_b
$HOME/src2/bitbucket/terraform/edge/stacks/a104_11_pci_fortigate_configure_a
$HOME/src2/bitbucket/terraform/edge/stacks/a104_11_pci_fortigate_configure_b
")
do
    (
    cd "$d"
    pwd
    rm -rf .terraform
    rm .terraform.lock.hcl
    rm terraform.log
    rm variables.mk
    terraform fmt
    )
done

git status | egrep .




##    update global shared files

cd ~/src2/bitbucket/terraform/edge/global_shared/
git checkout -f master --recurse-submodules
git pull --recurse-submodules


##    edit files as needed files

cd ~/src2/bitbucket/terraform/edge/stacks

code ~/src2/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_b/conf/addresses.yaml 






##    fmt all changed stacks

for d in $( echo "$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_X
")
do
    (
    cd "$d"
    pwd
    terraform fmt
    )
done



##    check if modules need updating

for d in $( echo "$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_X
")
do
    (
    cd "$d"
    pwd
    tfv check-module-versions
    )
done


##    save branch for plan on other systems

###   check expected terraform version

for d in $( echo "$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_X
")
do
    (
    cd "$d"
    pwd
    egrep -H 'required_version' terraform.tf
    )
done



##    create branch, save, and push code

branch_name=cr_22918_prod_move

git branch "$branch_name"
git checkout "$branch_name"
git add --all
git commit -m "NET-1837 cr_22918, fix route table advertisements and point all remaining NLBs to edge stack b firewalls"
git push



#███████████████████████████████████████████████████████████████████████████████████████████████████
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


###   execute plan and log

####    set branch & log info
branch_name=cr_22918_prod_move
branch_file=$(echo "$branch_name" | sed 's~/~_~g')
log_time=$(date +'%Y%m%d_%H%M')
action=plan   # plan or apply
type=full     # full or targeted


####  authenticate before running tfv - optional convenience
tfv vault-login


####    change to repo directory
cd ~/src2/bitbucket/terraform/edge/


####    pull clean copy of branch
git checkout -f master 
git status -s | egrep .
git status -s | egrep '^\?' | sed 's~^...~~g' | xargs -I '{}' rm -rf '{}'
git pull --recurse-submodules
git branch -df $branch_name
git checkout -f $branch_name
git pull --recurse-submodules


####    be sure there is a directoty ready to recieve logs
mkdir -p ~/mnt/data/logs/terraform_plan_apply


####    run plan and log it
stack=a104_05_edge_fortigate_configure_X
log_file=~/mnt/data/logs/terraform_plan_apply/${stack}_${log_time}_${branch_file}_${action}_${type}.log
cd $HOME/src2/bitbucket/terraform/edge/stacks/$stack
    start_time=$(date)
    { time tfv -t ~/bin/terraform_1.2.9 $action -no-color ; } 2>&1 | tee $log_file
    end_time=$(date)
    echo -e "\\n\\nstart time: $start_time"
    echo -e "log file: $log_file"
    egrep -i 'Apply complete!|^Plan:|Apply canceled.|Apply cancelled.|No changes\.' $log_file
    echo -e "end time: $end_time\\n\\n"

#   egrep -i 'Apply complete!|Creation complete|Destruction complete|Plan:|be create|be destroy|be replaced|^Error:|Enter a value:|Apply canceled.|Apply cancelled.| updated in-place|^real' $log_file



####    cleanup after run
git checkout -f $branch_name 
git status -s | egrep .
git status -s | egrep '^\?' | sed 's~^...~~g' | xargs -I '{}' rm -rf '{}'
git pull --recurse-submodules

for d in $( echo "$HOME/src2/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_X
")
do
    (
    cd "$d"
    pwd
    rm -rf .terraform
    rm .terraform.lock.hcl
    rm terraform.log
    rm variables.mk
    )
done


####    create PR, normal notes
Please ACK CR tasks when PR is approved.
Also, do not merge. Merge will happen when CR is executed.


####    attach plan logs to CR and note PR in security evidence 


#███████████████████████████████████████████████████████████████████████████████████████████████████
#---------------------------------------------------------------------------------------------------
#   apply terraform
#---------------------------------------------------------------------------------------------------
##    PR
https://scm.bestwestern.com/projects/TF/repos/edge/pull-requests/xxx/overview





##    authenticate before running tfv - optional convenience
tfv vault-login

##    authenticate to github before working with repo
#   open browser and loginto corpsso
#   open github enterprise
   
#   open cli
gh auth login
#   enter code from cli into browser
#   autherize github


##    verify approved change has been merged and working on clean code

cd ~/src/bitbucket/terraform/edge

git checkout -f master 
git status -s | egrep .
git status -s | egrep '^\?' | sed 's~^...~~g' | xargs -I '{}' rm -rf '{}'
git pull --recurse-submodules

for d in $( echo "$HOME/src/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_X
")
do
    (
    cd "$d"
    pwd
    rm -rf .terraform
    rm .terraform.lock.hcl
    rm terraform.log
    rm variables.mk
    )
done

git-sla -n 15


#   if branch has not been merged, merge branch and repull & verify



##    apply changes

mkdir -p ~/mnt/data/logs/terraform_plan_apply

branch_name=cr_22918_prod_move
branch_file=$(echo "$branch_name" | sed 's~/~_~g')
log_time=$(date +'%Y%m%d_%H%M')
action=apply  # plan or apply
type=full     # full or targeted




stack=a104_05_edge_fortigate_configure_X
log_file=~/mnt/data/logs/terraform_plan_apply/${stack}_${log_time}_${branch_file}_${action}_${type}.log
cd $HOME/src/bitbucket/terraform/edge/stacks/$stack
    start_time=$(date)
    { time tfv -t ~/bin/terraform_1.2.9 $action -no-color ; } 2>&1 | tee $log_file
    end_time=$(date)
    echo -e "\\n\\nstart time: $start_time"
    echo -e "log file: $log_file"
    egrep -i 'Apply complete!|^Plan:|Apply canceled.|Apply cancelled.|No changes\.' $log_file
    echo -e "end time: $end_time\\n\\n"

#   egrep -i 'Apply complete!|Creation complete|Destruction complete|Plan:|be create|be destroy|be replaced|^Error:|Enter a value:|Apply canceled.|Apply cancelled.| updated in-place|^real' $log_file



##    Attach apply logs to CR


##    cleanup after run

git checkout -f master 
git status -s | egrep .
git status -s | egrep '^\?' | sed 's~^...~~g' | xargs -I '{}' rm -rf '{}'
git pull --recurse-submodules

for d in $( echo "$HOME/src/bitbucket/terraform/edge/stacks/a104_05_edge_fortigate_configure_X
")
do
    (
    cd "$d"
    pwd
    rm -rf .terraform
    rm .terraform.lock.hcl
    rm terraform.log
    rm variables.mk
    )
done

#---------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#   security evidence

#---------------------------------------------------------------------------------------------------
##    PR
https://scm.bestwestern.com/projects/TF/repos/edge/pull-requests/xxx/overview

#---------------------------------------------------------------------------------------------------
##    Existing config






#---------------------------------------------------------------------------------------------------


#███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████


"""

print(template)
