import axios from "axios";

export const FETCHING = "FETCHING";
export const SUCCESS = "SUCCESS";
export const ERROR = "ERROR";
export const REFRESH = "REFRESH";
export const REFRESH_FALSE = "REFRESH_FALSE";

export const getUserData = id => {
  return dispatch => {
    dispatch({ type: FETCHING });
    axios
      .get(`${process.env.REACT_APP_BACKEND_URL}/api/users/fb/${id}`)
      .then(response => {
        dispatch({ type: SUCCESS, payload: response.data });
      })
      .catch(err => {
        dispatch({ type: ERROR, payload: "Error in getUserData API call" });
      });
  };
};

export const refreshMap = () => {
  return dispatch => {
    dispatch({ type: REFRESH, payload: true });
  };
};

export const refreshFalse = () => {
  return dispatch => {
    dispatch({ type: REFRESH_FALSE, payload: false });
  };
};
