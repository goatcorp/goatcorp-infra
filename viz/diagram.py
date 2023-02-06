from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import GCF
from diagrams.onprem.database import Postgresql
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.vcs import Github
from diagrams.programming.framework import React
from diagrams.programming.language import Csharp, Go, JavaScript, TypeScript
from third_party import Cloudflare, CloudflareAccess, CloudflareWorkers, Discord, Minio

with Diagram("goatcorp", show=False):
    with Cluster("Cloud"):
        merges_relay = GCF("Plugin Merges Relay")

        with Cluster("flare"):
            with Cluster("Workers"):
                plogon_dispatcher = CloudflareWorkers("Plogon Dispatcher")
                dalamud_feedback = CloudflareWorkers("Dalamud Feedback")

            cf_relay = Edge(color="darkorange")
            cf_dns = Cloudflare("DNS")
            cf_access = CloudflareAccess("Intranet Gateway")
            (
                cf_dns
                >> Edge(color="darkorange")
                >> [cf_access, plogon_dispatcher, dalamud_feedback, merges_relay]
            )

    with Cluster("NotNet"):
        with Cluster("bleatbot"):
            bleatbot = TypeScript("bleatbot")
            bleatbot >> SQL("SQLite")

        loggy = React("loggy")

    with Cluster("Franz"):
        franzbot = JavaScript("Franzbot")

    with Cluster("Hetzner Dedicated Server"):
        with Cluster("Caprine Operator"):
            Go("Caprine Operator") >> Postgresql("Database")

        with Cluster("Kamori"):
            kamori_cache = Redis("Cache")
            kamori_db = Postgresql("Database")
            kamori = Csharp("XLWebServices")
            kamori >> [kamori_cache, kamori_db]
            kamori_cdn = Minio("CDN")

        with Cluster("Monitoring Stack"):
            (
                cf_access
                >> cf_relay
                >> Grafana("Grafana")
                >> Prometheus("Prometheus")
                >> Edge(label="collect", style="dotted")
                >> kamori
            )

        (
            cf_dns
            >> cf_relay
            >> Nginx("nginx")
            >> Edge(color="darkgreen")
            >> [kamori, kamori_cdn]
        )

    with Cluster("GitHub"):
        plogon = Github("Plogon")
        helpy = Github("Helpy")
        faq = Github("FAQ")
        plogon >> Edge(color="black") >> cf_dns

    discord = Discord("Discord")
    (
        [plogon, dalamud_feedback]
        >> Edge(color="blue")
        >> discord
        >> Edge(color="blue", style="dashed")
        >> [franzbot, bleatbot]
    )

    (
        Rack("Client")
        >> Edge(color="red", style="dashed")
        >> [discord, helpy, loggy, faq, cf_dns]
    )
