from diagrams.custom import Custom


class Cloudflare(Custom):
    def __init__(self, label):
        cloudflare_icon = "resources/cf.png"
        super().__init__(label, cloudflare_icon)


class CloudflareAccess(Custom):
    def __init__(self, label):
        cf_access_icon = "resources/cf_access.png"
        super().__init__(label, cf_access_icon)


class CloudflareWorkers(Custom):
    def __init__(self, label):
        cf_workers_icon = "resources/cf_workers.png"
        super().__init__(label, cf_workers_icon)


class Discord(Custom):
    def __init__(self, label):
        discord_icon = "resources/discord.png"
        super().__init__(label, discord_icon)


class Minio(Custom):
    def __init__(self, label):
        minio_icon = "resources/minio.png"
        super().__init__(label, minio_icon)
