NIFCLOUD_DOC_BASE = 'https://pfs.nifcloud.com/api'


def get_document_site_url(service_id, operation_name):
    if service_id == "computing":
        link = '%s/rest/%s.htm' % (NIFCLOUD_DOC_BASE, operation_name)
    elif service_id == "storage":
        link = '%s/object-storage-service/%s.htm' % (NIFCLOUD_DOC_BASE,
                                                     operation_name)
    elif service_id == "devops-runner":
        link = '%s/devops/%s.htm' % (NIFCLOUD_DOC_BASE, operation_name)
    else:
        link = '%s/%s/%s.htm' % (NIFCLOUD_DOC_BASE, service_id, operation_name)

    return link
