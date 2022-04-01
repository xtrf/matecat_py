# coding: utf-8

"""
    MateCat API

    We developed a set of Rest API to let you integrate Matecat in your translation management system or in any other application. Use our API to create projects and check their status.  # noqa: E501

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import matecat_api
from matecat_api.api.project_api import ProjectApi  # noqa: E501
from matecat_api.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_change_project_password_post(self):
        """Test case for api_change_project_password_post

        Change password  # noqa: E501
        """
        pass

    def test_api_status_get(self):
        """Test case for api_status_get

        Retrieve the status of a project  # noqa: E501
        """
        pass

    def test_api_v1_new_post(self):
        """Test case for api_v1_new_post

        Create new Project on Matecat in detached mode  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_active_post(self):
        """Test case for api_v2_projects_id_project_password_active_post

        Active API  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_archive_post(self):
        """Test case for api_v2_projects_id_project_password_archive_post

        Archive API  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_cancel_post(self):
        """Test case for api_v2_projects_id_project_password_cancel_post

        Cancel API  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_completion_status_get(self):
        """Test case for api_v2_projects_id_project_password_completion_status_get

        Shows project completion statuses  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_creation_status_get(self):
        """Test case for api_v2_projects_id_project_password_creation_status_get

        Shows creation status of a project  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_due_date_delete(self):
        """Test case for api_v2_projects_id_project_password_due_date_delete

        Delete due date  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_due_date_post(self):
        """Test case for api_v2_projects_id_project_password_due_date_post

        Create due date  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_due_date_put(self):
        """Test case for api_v2_projects_id_project_password_due_date_put

        Update due date  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_get(self):
        """Test case for api_v2_projects_id_project_password_get

        Get project information  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post(self):
        """Test case for api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post

        Split Job  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post(self):
        """Test case for api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post

        Split Check  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_jobs_id_job_merge_post(self):
        """Test case for api_v2_projects_id_project_password_jobs_id_job_merge_post

        Merge  # noqa: E501
        """
        pass

    def test_api_v2_projects_id_project_password_urls_get(self):
        """Test case for api_v2_projects_id_project_password_urls_get

        Urls of a Project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
