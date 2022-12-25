package main

import "fmt"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}
func preorderTraversal(root *TreeNode) (res []int){
	// 前序遍历
	var traversal func(node *TreeNode)
	traversal = func(node *TreeNode) {
		if node == nil {
			return
		}
		res = append(res, node.Val)
		traversal(node.Left)
		traversal(node.Right)
	}
	traversal(root)
	return res
}

func inorderTraversal(root *TreeNode) (res []int){
	// 中序遍历
	var traversal func(node *TreeNode)
	traversal = func(node *TreeNode) {
		if node == nil {
			return
		}
		traversal(node.Left)
		res = append(res, node.Val)
		traversal(node.Right)
	}
	traversal(root)
	return res
}

func postorderTraversal(root *TreeNode) (res []int){
	// 后序遍历
	var traversal func(node *TreeNode)
	traversal = func(node *TreeNode) {
		if node == nil {
			return
		}
		traversal(node.Left)
		traversal(node.Right)
		res = append(res, node.Val)
	}
	traversal(root)
	fmt.Printf("%v", res)
	return res
}

func main() {
	var root TreeNode
	root.Val = 1
	root.Left = nil
	root.Right = nil
	preorderTraversal(&root)

}