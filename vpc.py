import boto.vpc
import time

class VPC():
    def establish_connection(self):
        region_name = input("enter your region: ")
        ami_id = input("enter your ami_id: ")
        conn = boto.vpc.connect_to_region(region_name)

    ##Vpc resource
    def vpc_resource(self):
        vpc_cidr = input("enter the CIDR Block range you'd like for your vpc: ")
        subnet_cidr = input("enter the CIDR Block range for any subnets: ")
        internal_ip = input("Ip of your company? ")
        vpc = conn.create_vpc(CidrBlock=vpc_cidr)
        subnetA = conn.create_subnet(VpcId=vpc.id, CidrBlock=subnet_cidr)
        secGroup = conn.create_security_group(GroupName='test_group',
                                              Description='Allows SSH for internal ips.',
                                              VPCId=vpc.id)
        secGroup.authorize_ingress(
            ip_protocol='tcp',
            from_port=22,
            to_port=22,
            cidr_ip=internal_ip
        )

    ##Internet GateWay and attach to vpc:
    def internet_gateway_resource(self):
        igw = conn.create_internet_gateway()
        conn.attach_internet_gateway(gateway.id, vpc.id)

    ##create your route to the internet:
    def route_table_resource(self):
        route_table = conn.create_route_table(route_table.id, subnetA.id)
        conn.associate_route_table(route_table.id, '0.0.0.0/0', igw.id)
